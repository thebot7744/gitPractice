from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index3():
    return render_template("index4.html")

@app.route("/qwerty", methods=["POST"])

def hello():
    name = request.form.get("name")
    return render_template("index5.html", name=name)

