import pytest

from muse import Muse


@pytest.fixture()
def muse():
    return Muse()


@pytest.fixture()
def client(muse):
    return muse.test_session()


def test_basic_route(muse):
    @muse.route("/home")
    def home(req, resp):
        resp.text = "HOME"


def test_route_duplicate_throws_exception(muse):
    @muse.route("/home")
    def home(req, resp):
        resp.text = "HOME"

    with pytest.raises(AssertionError):
        @muse.route("/home")
        def home2(req, resp):
            resp.text = "HOME"


def test_paramaterized_route(muse, client):
    @muse.route('/profile/{name}')
    def profile(req, resp, name):
        resp.text = f"Username {name}"

    assert client.get('http://testserver/profile/bmwasaru').text == "Username bmwasaru"
    assert client.get('http://testserver/profile/zero').text == "Username zero"


def test_muse_test_client_can_send_requests(muse, client):
    response_text = "AWESOME"

    @muse.route('/hello')
    def hello(req, resp):
        resp.text = response_text

    assert client.get('http://testserver/hello').text == response_text


def test_default_404_response(client):
    response = client.get('http://testserver/wfh')

    assert response.status_code == 404
    assert response.text == "Not found."
