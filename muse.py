import re


class wsgiapp:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        return self.delegate()

    def delegate(self):
        path = self.environ['PATH_INFO']
        method = self.environ['REQUEST_METHOD']

        for pattern, name in self.urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                # matched groups as arguments
                args = m.groups()
                funcname = method.upper() + "_" + name
                func = getattr(self, funcname)
                return func(*args)
        return self.not_found()


class application:


    urls = [
        ("/", "index"),
        ("/hello/(.*)", "hello")
    ]

    def index(self):
        status = "200 OK"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Welcome!\n"

    def hello(self, name):
        status = "200 OK"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Hello %s\n" % name

    def not_found(self):
        status = "404 Not Found"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Not Found!\n"