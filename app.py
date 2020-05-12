from muse.api import API

app = API()


@app.route('/home')
def home(request, response):
    response.text = "Hello, here is home"


@app.route('/about/')
def about(request, response):
    response.text = "This is the about page"
