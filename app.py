from flask import Flask, render_template, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BsssSuks'
socketio = SocketIO(app)
chatList = []

@socketio.on('message')
def message(msg):
    chatList.append(msg)
    if len(chatList) > 10:
        chatList.pop(0)
    socketio.send(msg)

@app.route('/chat', methods=['GET'])
def chatPage():
    return render_template('chat.html', l=chatList, u= request.values.get('q'))

@app.route('/')
def userPage():
    return render_template('user.html')

if __name__ == "__main__":
    socketio.run(app)    