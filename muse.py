import re
import traceback


class wsgiapp:
    """Base class for my wsgi application."""
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.status = "200 OK"
        self._headers = []

    def header(self, name, value):
        self._headers.append((name, value))

    def __iter__(self):
        try:
            x = self.delegate()
            self.start(self.status, self._headers)
        except:
            headers = [('Content-type', 'text/html')]
            self.start("500 Internal Error", headers)
            x = "Internal Error:\n\n" + traceback.format_exc()

        # return iter in either string or list type of the return value
        if isinstance(x, str):
            return iter([x])
        else:
            return iter(x)

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


class application(wsgiapp):

    urls = [
        ("/", "index"),
        ("/hello/(.*)", "hello")
    ]

    def index(self):

        self.header('Content-type', 'text/html')
        yield "Welcome!\n"

    def hello(self, name):
        self.header('Content-type', 'text/html')
        yield "Hello %s\n" % name

    def not_found(self):
        status = "404 Not Found"
        response_headers = [('Content-type', 'text/html')]
        self.start(status, response_headers)
        yield "Not Found!\n"