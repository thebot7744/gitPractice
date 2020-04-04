import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def homepage():
    return render_template("index3.html")
@app.route("/headline")

def index0():
    headline = "Hello, World!!"
    return render_template("index0.html", headline=headline)

@app.route("/bye")

def bye():
    headline = "Goodbye!"
    return render_template("index0.html", headline=headline)

@app.route("/date")

def index1():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 5
    return render_template("index1.html", new_year=new_year)

@app.route("/loop")

def index2():
    names = ["Alice", "Jim", "Charlotte"]
    return render_template("index2.html", names=names)



