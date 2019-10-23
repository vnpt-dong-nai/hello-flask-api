import os, sys, datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome_to_flask_api():
    return 'Hello, Welcome to Flask API!'

@app.route('/dora')
def return_string_doraemon():
    return 'doraemon'

@app.route('/info')
def return_json_object():
    return { 'current-time': datetime.datetime.now(), 'a-number': 1234 }

if __name__ == '__main__':
    app.run(host='localhost', port=1234)