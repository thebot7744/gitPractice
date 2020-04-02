from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    headline = "Hello, World!!"
    return render_template("index0.html", headline=headline)

@app.route("/bye")

def bye():
    headline = "Goodbye!"
    return render_template("index0.html", headline=headline)
