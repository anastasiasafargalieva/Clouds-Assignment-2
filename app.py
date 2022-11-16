from flask import Flask
from math import sin
from numerical_integration import trapezoid


app = Flask(__name__)
N = [5, 10, 100, 1000, 10000, 100000, 1000000]

@app.route("/")
def default():
    return "Hello, world!"

@app.route("/numericalintegralservice/<lower>/<upper>")
def integration(lower, upper):
    results = []
    for n in N:
        results.append(trapezoid(float(lower), float(upper), n))
    return str(results)