from tinyweb.server import webserver
from smartcube.hardware import Hardware
import logging
log = logging.getLogger(__name__)

def Server(hardware: Hardware) -> webserver:
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
            await resp.send_file("static/js/{}.gz".format(fn), content_type="application/javascript", content_encoding="gzip")


        # The same for css files - e.g.
        # Raw version of bootstrap.min.css is about 146k, compare to gzipped version - 20k
        @app.route("/css/<fn>")
        async def files_css(req, resp, fn):
            await resp.send_file("static/css/{}.gz".format(fn), content_type="text/css", content_encoding="gzip")


        # Images
        @app.route("/images/<fn>")
        async def files_images(req, resp, fn):
            log.debug("%s \n %s", req, fn)
            await resp.send_file("static/images/{}".format(fn), content_type="image/jpeg")


        # RESTAPI: System status
        class Status:
            def get(self, data):
                return {"memory": hardware.memory, "storage": hardware.storage, "network": hardware.network}

        log.debug("end configure webui")
        log.debug("start configure restapi")
        # RESTAPI: GPIO status
        class GPIOList:
            def get(self, data):
                res = []
                for p, d in hardware.pins.items():
                    res.append({"gpio": p, "nodemcu": d, "value": hardware.Ppin(p).value()})
                return {"pins": res}


        # RESTAPI: GPIO controller: turn PINs on/off
        class GPIO:
            def put(self, data, pin):
                # Check input parameters
                if "value" not in data:
                    return {"message": '"value" is requred'}, 400
                # Check pin
                pin = int(pin)
                if pin not in hardware.pins:
                    return {"message": "no such pin"}, 404
                # Change state
                val = int(data["value"])
                hardware.Pin(pin).val
                return {"message": "changed", "value": val}

        app.add_resource(Status, "/api/status")
        app.add_resource(GPIOList, "/api/gpio")
        app.add_resource(GPIO, "/api/gpio/<pin>")
        log.debug("end configure restapi")
        log.debug("end configure webserver")
        return app
        