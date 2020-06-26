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
    name = data['username']
    #return render_template(#something to be determined)

@socketio.on('submit message')
def send_message(data):
    comment = data['message']
    emit('vote totals', name, broadcast=True)


