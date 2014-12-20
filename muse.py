class application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    urls = [
        ("/", "index"),
        ("/hello", "hello")
    ]

    def __iter__(self):
        path_info = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for path, name  in self.urls:
            if path == path_info:
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func()
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