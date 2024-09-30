from flask import Flask

app = Flask(__name__)

import <your app module name>.views

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"