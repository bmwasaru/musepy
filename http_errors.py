from urllib.parse import urljoin

__all__ = [
    "header",
    "ctx",
]


class HTTPError(Exception):
    def __init__(self, status, headers={}, data=""):
        ctx.status = status
        for k, v in headers.items():
            header(k, v)
        self.data = data
        Exception.__init__(self, status)


def _status_code(status, data=None, classname=None, docstring=None):
    if data is None:
        data = status.split(" ", 1)[1]
    classname = status.split(" ", 1)[1].replace(
        " ", ""
    )
    docstring = docstring or "`%s` status" % status

    def __init__(self, data=data, headers={}):
        HTTPError.__init__(self, status, headers, data)

    return type(
        classname, (HTTPError, object), {'__doc__': docstring, "__init__":__init__}
    )


ok = OK = _status_code("200 OK", data="")
created = Created = _status_code("201 Created")
accepted = Accepted = _status_code("202 Accepted")
nocontent = NoContent = _status_code("204 No Content")


class Redirect(HTTPError):
    """ `301 Moved Permanently` redirect."""

    def __init__(self, url, status="301 Moved Permanently", absolute=False):
        """
        Returns a `status` redirect to the new URL.
        `url` is joined with the base URL
        """
        newloc = urljoin(ctx.path, url)

        if newloc.startswith("/"):
