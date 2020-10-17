# debugger.py
from os import getenv


def initialize_flask_server_debugger_if_needed():
    print(getenv("DEBUGGER"))
    if getenv("DEBUGGER") == "True":
        import multiprocessing
        import debugpy
        if multiprocessing.current_process().pid > 1 and not debugpy.is_client_connected():

            debugpy.listen(("0.0.0.0", 10001))
            print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳", flush=True)
            debugpy.wait_for_client()
            print("🎉 VS Code debugger attached, enjoy debugging 🎉", flush=True)