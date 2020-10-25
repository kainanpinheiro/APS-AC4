from flask import Flask
from retry.api import retry_call
import requests

app = Flask(__name__)


def api_call(service):
    r = requests.get(service)
    if r.status_code != 200:
        raise Exception("Not found")
    return r.text


@app.route("/")
def index():
    r = retry_call(api_call, fargs=["http://localhost:5000"])
    return r


if __name__ == "__main__":
    app.run(port=3000)
