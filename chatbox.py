import os
import requests

from flask import *
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

comment = {'name': '', 'comment': ''}


@app.route('/')
def username():
    return render_template('comment0.html', comment=comment)


@socketio.on('submit name')
def chat_room(data):
    user = data['name']
    comment['name'] = user
    return render_template('test.html', name=user)

@socketio.on('submit message')
def send_message(data):
    message = data['message']
    emit('vote totals', message, broadcast=True)


