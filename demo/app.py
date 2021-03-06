from muse import Muse
from muse.middleware import Middleware

app = Muse()


def custom_exception_handler(request, response, exception_cls):
    response.text = "Oopsy! Something went wrong."


class SimpleMiddleware(Middleware):
    def process_request(self, req):
        print("Processing request", req.url)

    def process_response(self, req, resp):
        print("Processing response", req.url)


app.add_exception_handler(custom_exception_handler)
app.add_middleware(SimpleMiddleware)


@app.route('/exception')
def exception(request, response):
    response.text = app.template('oopsy.html')


@app.route('/home')
def home(request, response):
    response.text = "Hello, here is home"


@app.route('/about/')
def about(request, response):
    response.text = "This is the about page"


@app.route('/profile/{name}')
def profile(request, response, name):
    response.text = f"Hello {name}"


@app.route('/users/')
class UsersHandler:
    def get(self, request, response):
        response.text = "Users handler"


@app.route('/username/{name}')
def username(req, resp, name):
    resp.text = app.template("test_example.html", context={'name': 'bmwasaru'})
