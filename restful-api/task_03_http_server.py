from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    # -------------------------
    # GET REQUEST HANDLER
    # -------------------------
    def do_GET(self):

        # ROOT ENDPOINT
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # DATA ENDPOINT
        if self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
            return

        # STATUS ENDPOINT
        if self.path == "/status":
            data = {"status": "OK"}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
            return

        # INFO ENDPOINT
        if self.path == "/info":
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
            return

        # -------------------------
        # 404 NOT FOUND
        # -------------------------
        self.send_response(404)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        error = {"error": "Endpoint not found"}
        self.wfile.write(json.dumps(error).encode())


# -------------------------
# START SERVER
# -------------------------
def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)

    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
