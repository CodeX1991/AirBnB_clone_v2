#!/usr/bin/python3
"""
A Flask web application
"""

from flask import Flask, render_template

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


# Handle variable section
@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace('_', ' ')


# Handle variable section
@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    return "Python " + text.replace('_', ' ')


# Handle variable section
@app.route("/number/<int:n>", strict_slashes=False)
def is_n_number(n):
    return "{:d} is a number".format(n)


# Handle variable section
@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    # Execute app
    app.run(host='0.0.0.0', port=5000)
