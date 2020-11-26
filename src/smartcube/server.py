from tinyweb.server import webserver
from smartcube.hardware.board import Board
from smartcube.models import Handler, Wifi, Model
import logging
import json

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

    @app.resource("/api/v1/handler/side/<side_id>", "GET")
    def handler_side_get(data, side_id):
        """
        :param side_id:
        :type side_id: dict | bytes

        :rtype: Handler as json
        """
        import ujson as json

        with open("/handlers.json", "r") as f:
            handler_dict = json.loads(f.read())
        log.debug(handler_dict)
        h = Handler.from_dict(handler_dict)
        log.debug(h)
        d = Model.JSONEncodeModel(h)
        log.debug(d)
        with open("/handlers_writen.json", "w") as f:
            f.write(json.dumps(d, indent=4))
        return d

    class APIView:
        """
        Convenience class for creating a restfull router vie tinyweb

        """

        def get(self, data, id):
            raise NotImplementedError

        def put(self, data, id):
            raise NotImplementedError

        def delete(self, data, id):
            raise NotImplementedError

        def list(self, data):
            raise NotImplementedError

        def post(self, data):
            raise NotImplementedError

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
                    return cls.list(self, data)

                def post(self, data):
                    return cls.post(self, data)

            class tmp_id:
                def get(self, data, id):
                    return cls.get(self, data)

                def put(self, data, id):
                    return cls.put(self, data)

                def delete(self, data, id):
                    return cls.delete(self, data)

            ressource_name = cls.__name__[0:-4].lower()

            app.add_resource(tmp_list, "{}/{}".format(path, ressource_name))
            app.add_resource(tmp_id, "{}/{}/<id>".format(path, ressource_name))

    class WifiView(APIView):
        def get(self, data, id):
            """
            :rtype: return Wifi as json
            """
            return Model.JSONEncodeModel(Wifi.get_by_id(id))
        # TODO: #5 othe methods

        def post(self, data):
            wifi = Wifi.from_dict(data)
            wifi.save()

        def delete(self, data, id):
            Wifi.delete(id)

        def list(self, data):
            """
            :rtype: Wifi list as json
            """
            wifis = [Model.JSONEncodeModel(wifi)['ssid']
                     for wifi in Wifi.get_all()]
            wifis = json.dumps(wifis)
            return wifis

    app.add_resource(Status, "/api/v1/status")
    app.add_resource(GPIOList, "/api/v1/gpio")
    app.add_resource(GPIO, "/api/v1/gpio/<pin>")
    app.add_resource(WifiView, "/api/v1/system/config/wifi")
    WifiView.add_APIView_router(app, "/api/v1/")
    log.debug("end configure restapi")
    log.debug("end configure webserver")
    return app
