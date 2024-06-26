#!/usr/bin/python3
"""
Run an app with Flask web framework
"""

from flask import Flask

myApp = Flask(__name__)


@myApp.route("/", strict_slashes=False)
def homepage():
    return "Hello HBNB!"


@myApp.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@myApp.route("/c/<text>", strict_slashes=False)
def textvariable(text):
    text = text.replace("_", " ")
    return f"C {text}"


@myApp.route('/python/', strict_slashes=False)
@myApp.route('/python/<text>', strict_slashes=False)
def text_variable(text="is_cool"):
    text = text.replace("_", " ")
    return f"python {text}"


if __name__ == "__main__":
    myApp.run(host='0.0.0.0', port=5000)
