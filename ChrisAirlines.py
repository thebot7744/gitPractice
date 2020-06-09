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

@app.route("/book", methods=["POST"])
def book():
    name = request.form.get("name")
    if name is '':
        return render_template("index8.html", message="Please enter passenger name.")
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

@app.route("/flights")
def display_flights():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index10.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    flight = db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).fetchone()

    if flight is None:
        return render_template("index8.html", message="No such flight.")

    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :fi", {"fi": flight_id}).fetchall()

    return render_template("index11.html", flight=flight, passengers=passengers)


