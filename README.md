# Muse, a python web micro framework

A small web framework built for learning purposes

## Setup
You need to install the requirements in a virtual environment
```bash
virtualenv venv -p python3
pip install -r requirements.txt
```

## Running tests
```bash
pytest test_muse.py
```

## Running the demo app

The demo application is in example directory

To run the demo you need to install the framework. This can be done in the root directory of this repository as follows:
```bash
python setup.py install
```

Change the directory to the example folder
```bash
cd example
gunicorn app:app
```

## Framework usage
```python
from muse import Muse

app = Muse()


@app.route('/')
def home(res, resp):
    resp.text = "Hello World"

```

You can also use Django style routing to match functions to http request path

```python
from muse import Muse

app = Muse()


def home(req, resp):
    resp.text = "Hello World"
    
app.add_route('/', home)

```
