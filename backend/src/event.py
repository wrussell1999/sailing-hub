from backend.src.app import app
from flask import Flask, request, jsonify

@app.route('/event/<event_id>')
def view_event(event_id):
    pass


@app.route('/event/<event_id>/update')
def update_event(event_id):
    pass


@app.route('/event/<event_id>/delete')
def delete_event(event_id):
    pass


@app.route('/enter/<event_id>')
def enter_event(event_id):
    pass


@app.route('/enter/<event_id>/update')
def update_entry(event_id):
    pass


@app.route('/enter/<event_id>/delete')
def delete_entry(event_id):
    pass


@app.route('/enter/<event_id>/view')
def entries(event_id):
    pass


@app.route('/enter/<event_id>/export')
def export_entries(event_id):
    pass
