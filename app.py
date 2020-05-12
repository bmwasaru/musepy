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
