from http.server import HTTPServer, CGIHTTPRequestHandler


class Server():
    def __init__(self, host, port):
        self.server_address = (host, port)

    def http_server(self):
        httpd = HTTPServer(self.server_address, CGIHTTPRequestHandler)
        httpd.serve_forever()


server = Server('', 8888)
server.http_server()