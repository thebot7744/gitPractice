import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("sqlite:////Users/christopherwang/Documents/GitHub/gitPractice/base1.db")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index7.html", flights=flights)

@app.route("/flight_details")
def display_all():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index10.html", flights=flights)

@app.route("/passengers")
def passengers():
    password = str(request.form.get("password"))
    if password == '123':
        flights = db.execute("SELECT * FROM passengers").fetchall()
        return render_template("index11.html", flights=flights)
    else:
        return render_template("index8.html", message="WRONG PASSWORD")

@app.route("/holdingroom")
def holding_room():
    return render_template("index12.html")



@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("index8.html", message="INVALID FLIGHT ID NUMBER")

    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("index8.html", message="NO SUCH FLIGHT WITH THAT ID")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
               {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("index9.html", message="You have successfully booked your flight!")


