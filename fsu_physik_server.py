#!/usr/bin/env python3
from fsu_physik import server, common
import logging
from logging import handlers
import os, sys
from pythonjsonlogger import jsonlogger
import argparse
import webbrowser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Attack Helper for Die Staemme")
    parser.add_argument("--host", help="Bind the server on this address", default="127.0.0.1")
    parser.add_argument("--port", help="Bind the server on this port", default=5001)
    parser.add_argument("--allow-root", help="Allow to start server with root or sudo", action="store_true")
    parser.add_argument("--open-browser", help="Open browser tab with dashboard after startup", action="store_true")
    args = parser.parse_args()

    if "getuid" in dir(os) and os.getuid() == 0 and not args.allow_root:
        print("Starting DS_Timer as root or with sudo is disabled. Use --allow-root")
        sys.exit(1)
        print("hey")
    common.create_folder_structure()

    # init logger
    log_dir = os.path.join(common.get_root_folder(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "dstimer.log")
    logger = logging.getLogger("dstimer")
    logger.setLevel(logging.DEBUG)
    handler = handlers.TimedRotatingFileHandler(log_path, when="D")
    formatter = jsonlogger.JsonFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if args.open_browser:
        webbrowser.open("http://127.0.0.1:" + str(args.port), new=2)

    #send_action.DaemonThread().start()
    server.app.run(host=args.host, port=args.port)
