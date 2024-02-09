from backend.src.app import app
from flask import Flask, request, jsonify

@app.route('/race/<race_id>/')
def view_race(race_id):
    pass

@app.route('/race/<race_id>/lap_time')
def add_lap_time(race_id):
    pass

@app.route('/race/<race_id>/start_time')
def add_start_time(race_id):
    pass

@app.route('/race/<race_id>/end_time')
def add_end_time(race_id):
    pass