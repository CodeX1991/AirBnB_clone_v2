#!/usr/bin/python3
"""
A Flask web application
"""

from flask import Flask

# Create an instance of the Flash class
app = Flask(__name__)


# Tell Flask what URL should trigger our function
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Handle subfolder
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    # Execute app
    app.run(host='0.0.0.0', port=5000)
