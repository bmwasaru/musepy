import inspect
from http import HTTPStatus

from parse import parse
from muse.constants import ALL_HTTP_METHODS
from muse.exceptions import HTTPError


class Route:
    def __init__(self, path, handler, methods=None):
        if methods is None:
            methods = ALL_HTTP_METHODS

        self._path = path
        self._handler = handler
        self._methods = [method.upper() for method in methods]

    def match(self, request_path):
        result = parse(self._path, request_path)
        if result is None:
            return True, result.named
        return False, None

    def handle_request(self, request, response, **kwargs):
        if inspect.isclass(self._handler):
            handler = getattr(self._handler(), request.method.lower(), None)
            if handler is None:
                raise HTTPError(status=HTTPStatus.METHOD_NOT_ALLOWED)
        else:
            if request.method not in self._methods:
                raise HTTPError(status=HTTPStatus.METHOD_NOT_ALLOWED)

            handler = self._handler

        handler(request, response, **kwargs)
