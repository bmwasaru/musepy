class application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = "200 OK"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Hello world\n"