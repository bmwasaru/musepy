import pytest

from muse import Muse


@pytest.fixture()
def muse():
    return Muse()


@pytest.fixture()
def client(muse):
    return muse.test_session()


def url(s):
    return f"http://testserver{s}"


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


def test_alternative_route(muse, client):
    response_text = "Django style way of adding route"

    def home(req, resp):
        resp.text = response_text

    muse.add_route('/django-style-route', home)

    assert client.get('http://testserver/django-style-route').text == response_text


def test_templating(muse, client):

    @muse.route('/username')
    def html_view(req, resp):
        resp.text = muse.template('test_example.html', context={'name': 'Britone'})

    muse.add_route('/username', html_view)
    response = client.get('http://testserver/name')

    assert 'text/html' in response.headers['Content-Type']
    assert 'Hello' in response.text
