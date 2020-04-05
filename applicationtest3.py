from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def index3():
    return render_template("index4.html")

@app.route("/qwerty", methods=["GET", "POST"])

def hello():
    if request.method == "GET":
        return "Please submit the form."
    else:
        name = request.form.get("name")
        names = name.capitalize()
        return render_template("index5.html", name=names)

