import flask
from flask import Flask, jsonify, request
import time
from datetime import datetime

App_name = 'Milan Messenger'
app = Flask(App_name)

db = [
    {
    "text": "First message",
    "time": time.time(),
    "name": "Admin"
    }
]

@app.route("/")
def start():
    return App_name

@app.route("/status")
def status():
    names = []
    for i in db:
        names.append((i['name']))
    set_names = len(set(names))
    len_db = len(db)
    status = {
        'status ': True,
        'name ': App_name,
        'time ': datetime.now(),
        'number of messages ': len_db,
        'number of users ': set_names
    }
    return jsonify(status)


@app.route("/send", methods=['POST'])
def send_messages():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if name =='' or text =='':
        return abort(400)

    message = {
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)
    return {"ok": True}

@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)

    return {'messages': messages[:100]}

app.run()












































































































