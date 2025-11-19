import sublime
import sublime_plugin
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

INPUT_PATH = r"PUT YOUR PATH HERE"
OUTPUT_PATH = r"PUT YOUR PATH HERE"
EXPECTED_PATH = r"PUT YOUR PATH HERE"

server_instance = None


class CCRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_len = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_len).decode('utf-8')

            data = json.loads(body)

            tests = data.get("tests", [])

            if len(tests) == 0:
                print("CompetitiveHelper: No tests received")
                return

            # Only first test
            input_data = tests[0].get("input", "")
            expected_output = tests[0].get("output", "")

            # Write input
            with open(INPUT_PATH, "w", encoding="utf-8") as f:
                f.write(input_data)

            # Clear output file
            with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
                f.write("")

            # Write expected output
            with open(EXPECTED_PATH, "w", encoding="utf-8") as f:
                f.write(expected_output)

            print("CompetitiveHelper: Test case saved!")

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        except Exception as e:
            print("CompetitiveHelper: ERROR ->", e)


class StartCcServerCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        global server_instance

        if server_instance:
            print("CompetitiveHelper: Server already running.")
            return

        def server_thread():
            global server_instance
            server_instance = HTTPServer(('127.0.0.1', 10045), CCRequestHandler)
            print("CompetitiveHelper: Listening on 127.0.0.1:10045")
            server_instance.serve_forever()

        thread = threading.Thread(target=server_thread, daemon=True)
        thread.start()
        print("CompetitiveHelper: Server started")

