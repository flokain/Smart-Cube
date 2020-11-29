from tinyweb.server import webserver, HTTPException
from smartcube.hardware.board import Board
from smartcube.models import Handler, Wifi, Model
import logging
import ujson as json

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

    class APIView:
        """
        Convenience class for creating a restfull router vie tinyweb

        """
        class Meta:
            model = Model
            # TODO: #6 implement read and write only field specification
            # DRF:  extra_kwargs = {'password': {'write_only': True}}
            # DRF:  extra_kwargs = {'password': {'read_only': True}}

        resource_name = Meta.model.__name__.lower()

        @classmethod
        def get(cls, data, id):
            """
            :rtype: return Wifi as json
            """
            return Model.JSONEncodeModel(cls.Meta.model.get_by_id(id))

        @classmethod
        def list(cls, data):
            return json.dumps(Model.JSONEncodeModelList(cls.Meta.model.get_all()))

        @classmethod
        def post(cls, data):
            obj = cls.Meta.model.from_dict(data)
            obj.save()
            return obj.JSONEncodeModel(obj)

        @classmethod
        def put(cls, data, id):
            obj = cls.Meta.model.from_dict(data)
            obj.save(id)
            return obj.JSONEncodeModel(obj)

        @classmethod
        def delete(cls, data, id):
            cls.Meta.model._delete(id)

        @classmethod
        def add_APIView_router(cls, app: webserver, path: str):
            """
            generates router analogue to django restframeworks viewset routers
            <path>/<classname w/o View suffix> supports get and post
            <path>/<classname w/o View suffix>/<id> supports get, put and delete

            Args:
                app (webserver): the tinyweb server to add routes to
                path (str): base bath for the router
            """
            class tmp_list:
                def get(self, data):
                    return cls.list(data)

                def post(self, data):
                    return cls.post(data)

            class tmp_id:
                def get(self, data, id):
                    try:
                        return cls.get(data, id)
                    except KeyError:
                        raise HTTPException(404)

                def put(self, data, id):
                    try:
                        return cls.put(data, id)
                    except KeyError:
                        raise HTTPException(404)

                def delete(self, data, id):
                    try:
                        cls.delete(data, id)
                    except KeyError:
                        raise HTTPException(404)

            list_string = "{}/{}".format(path, cls.resource_name)
            log.debug("adding route {}".format(list_string))
            app.add_resource(
                tmp_list, "{}/{}".format(path, cls.resource_name))

            res_string = "{}/{}/<id>".format(path,
                                             cls.resource_name)
            log.debug("adding route {}".format(res_string))
            app.add_resource(
                tmp_id, "{}/{}/<id>".format(path, cls.resource_name))

    class WifiView(APIView):
        class Meta:
            model = Wifi

    class HandlerView(APIView):
        class Meta:
            model = Handler
            # TODO: #9 find a better path for all handlers

        resource_name = "{}/side".format(Meta.model.__name__.lower())

    app.add_resource(Status, "/api/v1/status")
    app.add_resource(GPIOList, "/api/v1/gpio")
    app.add_resource(GPIO, "/api/v1/gpio/<pin>")
    WifiView.add_APIView_router(app, "/api/v1/system/config")
    HandlerView.add_APIView_router(app, "/api/v1")
    log.debug("end configure restapi")
    log.debug("end configure webserver")
    return app
