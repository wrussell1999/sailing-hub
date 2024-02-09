from src import app
from flask import Flask, request, jsonify, g

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"ping": "pong"})

@app.route('/join')
def join():
    pass

@app.route('/login')
def login():
    pass

@app.route('/profile')
def profile():
    pass
