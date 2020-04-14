from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/<string:name>")
def hello_user(name):
    name = name.capitalize()
    return f"<h3>Hello, {name}!</h3>"

