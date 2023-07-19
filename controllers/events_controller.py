from flask import render_template, Blueprint, request
from models.event_list import event_list
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return "Hello World"
@events_blueprint.route('/events', methods=['POST'])
def add_event():
    pass