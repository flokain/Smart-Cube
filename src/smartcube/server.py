from tinyweb.server import webserver
from smartcube.hardware import board
from smartcube.models import Handler
import logging

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
                res.append({"gpio": p, "nodemcu": d, "value": board.Pin(p).value()})
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
    
    @app.resource("/api/v1/handler/side/<side_id>","GET")
    def handler_side_get(data,side_id):
        """
        :param side_id: 
        :type side_id: dict | bytes

        :rtype: Handler as json
        """
        import ujson as json
        from smartcube.encoder import JSONEncodeModel

        with open("/handlers.json", "r") as f:
            handler_dict = json.loads(f.read())
        log.debug(handler_dict )
        h = Handler.from_dict(handler_dict)
        log.debug(h)
        d = JSONEncodeModel(h)
        log.debug(d)
        with open("/handlers_writen.json", "w") as f:
            f.write(json.dumps(d, indent=4))
        return d


    app.add_resource(Status, "/api/v1/status")
    app.add_resource(GPIOList, "/api/v1/gpio")
    app.add_resource(GPIO, "/api/v1/gpio/<pin>")
    log.debug("end configure restapi")
    log.debug("end configure webserver")
    return app
