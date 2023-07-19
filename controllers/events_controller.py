from flask import render_template, Blueprint, request
from models.event_list import event_list
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route("/")
def index():
    return render_template("index.jinja", title = "Events Home")

@events_blueprint.route('/events')
def events():
    return render_template("events.jinja", title = "Events List", event_list = event_list)

@events_blueprint.route('/addevent')
def add_event():
    return render_template("add_event.jinja")