from http.server import BaseHTTPRequestHandler, HTTPServer
from subprocess import Popen


class MyServer(BaseHTTPRequestHandler):
    def __init__(self) -> None:
        super().__init__()
        self.auth_code = None

    def do_GET(self):
        global auth_code
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if "code=" in self.path:
            self.wfile.write(
                bytes(
                    "<html><head><title>Authorization Success</title></head>", "utf-8"
                )
            )
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Thank you for authorizing.</p>", "utf-8"))
            start = self.path.find("code=") + len("code=")
            end = self.path.find("&", start)
            self.auth_code = self.path[start:end]
        else:
            self.wfile.write(
                bytes(
                    "<html><head><title>Authorization Failure</title></head>", "utf-8"
                )
            )
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Authorization failed.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


def authenticate(client_id: str) -> str:
    global auth_code
    webServer = HTTPServer(("localhost", 8080), MyServer)

    Popen(
        [
            "open",
            f"http://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri=http://localhost%3A8080/exchange_token&approval_prompt=force&scope=read",
        ]
    )

    while True:
        webServer.handle_request()
        if webServer.auth_code:
            break

    webServer.server_close()

    return webServer.auth_code
