import logging
import ujson as json
from tinyweb.server import webserver
from tinyweb.server import HTTPException

from smartcube.hardware.board import Board
from smartcube.models.handler import Handler
from smartcube.models.wifi import Wifi
from smartcube.models.user import User
from smartcube.models.base_model import Model


log = logging.getLogger(__name__)


def Server(board: Board) -> webserver:
    log.debug("start configuring webserver")
    app = webserver()

    # Index page
    log.debug("start configure webui")

    @app.route("/")
    @app.route("/index.html")
    async def index(req, resp):
        await resp.send_file("static/index.html")

    # JS files.
    # Since ESP8266 is low memory platform - it totally make sense to
    # pre-gzip all large files (>1k) and then send gzipped version

    @app.route("/js/<fn>")
    async def files_js(req, resp, fn):
        await resp.send_file(
            "static/js/{}.gz".format(fn),
            content_type="application/javascript",
            content_encoding="gzip",
        )

    # The same for css files - e.g.
    # Raw version of bootstrap.min.css is about 146k, compare to gzipped version - 20k
    @app.route("/css/<fn>")
    async def files_css(req, resp, fn):
        await resp.send_file(
            "static/css/{}.gz".format(fn),
            content_type="text/css",
            content_encoding="gzip",
        )

    # Images
    @app.route("/images/<fn>")
    async def files_images(req, resp, fn):
        log.debug("%s \n %s", req, fn)
        await resp.send_file("static/images/{}".format(fn), content_type="image/jpeg")

    # RESTAPI: System status

    class Status:
        def get(self, data):
            return {
                "memory": board.memory,
                "storage": board.storage,
                "network": board.network,
            }

    log.debug("end configure webui")
    log.debug("start configure restapi")
    # RESTAPI: GPIO status

    class GPIOList:
        def get(self, data):
            res = []
            for p, d in board.pins.items():
                res.append({"gpio": p, "nodemcu": d,
                            "value": board.Pin(p).value()})
            return {"pins": res}

    # RESTAPI: GPIO controller: turn PINs on/off
    class GPIO:
        def put(self, data, pin):
            # Check input parameters
            if "value" not in data:
                return {"message": '"value" is requred'}, 400
            # Check pin
            pin = int(pin)
            if pin not in board.pins:
                return {"message": "no such pin"}, 404
            # Change state
            val = int(data["value"])
            board.Pin(pin).value(val)
            return {"message": "changed", "value": val}

    class APIViewParametrized:
        """
        Convenience class for creating a restfull router vie tinyweb

        """
        class Meta:
            model = Model
            # TODO: #6 implement read and write only field specification
            # DRF:  extra_kwargs = {'password': {'write_only': True}}
            # DRF:  extra_kwargs = {'password': {'read_only': True}}

        resource_name = '{}s'.format(Meta.model.__name__.lower())

        @classmethod
        def get(cls, data, id):
            """
            :rtype: return Wifi as json
            """
            try:
                return Model.JSONEncodeModel(cls.Meta.model.get_by_id(id))
            except KeyError:
                raise HTTPException(404)

        @classmethod
        def put(cls, data, id):
            obj = cls.Meta.model.from_dict(data)
            obj.save(id)

            return obj.JSONEncodeModel(obj)

        @classmethod
        def delete(cls, data, id):
            log.debug("deleting object with key {}".format(id))
            try:
                cls.Meta.model._delete(id)
                return id
            except KeyError:
                raise HTTPException(404)

    class APIView:
        """
        Convenience class for creating a restfull router vie tinyweb

        """
        class Meta:
            model = Model
            # TODO: #6 implement read and write only field specification
            # DRF:  extra_kwargs = {'password': {'write_only': True}}
            # DRF:  extra_kwargs = {'password': {'read_only': True}}

        resource_name = '{}s'.format(Meta.model.__name__.lower())

        @classmethod
        def get(cls, data):
            return json.dumps(Model.JSONEncodeModelList(cls.Meta.model.get_all()))

        @classmethod
        def post(cls, data):
            obj = cls.Meta.model.from_dict(data)
            obj.save()
            return obj.JSONEncodeModel(obj)

    class HandlerView(APIView):
        class Meta:
            model = Handler

        @classmethod
        def get(cls, data):
            return json.dumps(Model.JSONEncodeModelList(cls.Meta.model.get_all(data.get("event-id"))))

    class WifiView(APIView):
        class Meta:
            model = Wifi

    class WifiViewParametrized(APIViewParametrized):
        class Meta:
            model = Wifi

    class HandlerViewParametrized(APIViewParametrized):
        class Meta:
            model = Handler

    class UserView(APIView):
        class Meta:
            model = User

    class UserViewParametrized(APIViewParametrized):
        class Meta:
            model = User

    app.add_resource(Status, "/api/v1/status")
    app.add_resource(GPIOList, "/api/v1/gpio")
    app.add_resource(GPIO, "/api/v1/gpio/<pin>")

    app.add_resource(HandlerViewParametrized, "/api/v1/handlers/<id>")
    app.add_resource(HandlerView, "/api/v1/handlers")

    # /cube/state
    # /system/state
    # /system/jobs/
    # /system/jobs/id
    # /system/jobs/id/state

    # /system/config
    # /system/config/accespoint
    # /system/reboot
    # TODO: #17 update tiny web for any amount of params
    app.add_resource(WifiViewParametrized, "/api/v1/system/config/wifis/<id>")
    app.add_resource(WifiView, "/api/v1/system/config/wifis")

    app.add_resource(UserView, "/api/v1/users")
    app.add_resource(UserView, "/api/v1/users/<Userid>")
    log.debug("end configure restapi")
    log.debug("end configure webserver")
    return app
