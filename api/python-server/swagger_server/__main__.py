#!/usr/bin/env python3

import connexion
from swagger_server import encoder
import debugger

app = connexion.App(__name__, specification_dir="./swagger/")
app.app.json_encoder = encoder.JSONEncoder
app.add_api("swagger.yaml", arguments={"title": "Smartcube API"}, pythonic_params=True)

if __name__ == "__main__":
    debugger.initialize_flask_server_debugger_if_needed()
    app.run(port=8080)
