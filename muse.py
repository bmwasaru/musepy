class application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        path = self.environ['PATH_INFO']
        if path == '/':
            return self.index()
        elif path == '/hello':
            return self.hello()
        else:
            return self.not_found()

    def index(self):
        status = "200 OK"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Welcome!\n"

    def hello(self):
        status = "200 OK"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Hello world\n"

    def not_found(self):
        status = "404 Not Found"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Not Found!\n"