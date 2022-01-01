import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "My first image!!!@!"


@app.route("/container")
def container():
    return "Container running successfully"


if __name__ == "__main__":
    print("1st Image")
    app.run()
