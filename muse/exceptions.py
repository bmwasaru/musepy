from http import HTTPStatus


class HTTPError(Exception):
    def __init__(self, status):
        # status should be an integer
        assert isinstance(status, int)
        self._http_status = HTTPStatus(status)

    @property
    def status(self):
        return self._http_status.value
    
    @property
    def status_phrase(self):
        return self._http_status.phrase

    def __str__(self):
        # e.g 200 OK
        return f"{self.status} {self.status_phrase}"
