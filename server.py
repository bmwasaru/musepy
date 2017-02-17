from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080


class HelloWorld(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Hello World")
        return

try:
    server = HTTPServer(('', PORT_NUMBER), HelloWorld)
    print("Started server on port {}".format(PORT_NUMBER))
    server.serve_forever()
except KeyboardInterrupt as e:
    print("Shutting down server...")
    server.socket.close()
