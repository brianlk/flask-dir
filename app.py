from flask import Flask
from x import abc

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello, world!"

@app.route('/ok')
def test():
	y = abc()
	return y
