from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socket = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')
@socket.on('connect')
def connect():
    print("[CLIENT CONNECTED]:", request.sid)
@socket.on('disconnect')
def disconn():
    print("[CLIENT DISCONNECTED]:", request.sid)
@socket.on('notify')
def notify(user):
    emit('notify', user, broadcast=True, skip_sid=request.sid)
@socket.on('data')
def emitback(data):
    emit('returndata', data, broadcast=True)


if __name__ == "__main__":
    socket.run(app, port=8080)