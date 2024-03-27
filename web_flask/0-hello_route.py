#!/usr/bin/python3
"""
Run an app with Flask web framework
"""
from flask import Flask

myApp = Flask(__name__)
@myApp.route("/", strict_slashes=False)
def homepage():
    return "Hello HBNB!"

if __name__ == "__main__":
    myApp.run(host='0.0.0.0', port=5000)
