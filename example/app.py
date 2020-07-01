from muse import Muse

app = Muse()


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


if __name__ == '__main__':
    app
