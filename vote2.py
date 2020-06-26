import os
import requests

from flask import *
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

votes = {'yes': 0, 'no': 0, 'maybe': 0}


@app.route('/')
def index():
    return render_template('vote2.html', votes=votes)


@socketio.on('submit vote')
def vote(data):
    selection = data['selection']
    votes[selection] += 1
    emit('vote totals', votes, broadcast=True)
