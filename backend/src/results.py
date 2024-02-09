from backend.src.app import app
from flask import Flask, request, jsonify


@app.route('/results/<event_id>')
def results(event_id):
    pass
