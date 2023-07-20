from flask import render_template, Blueprint, request
from models.event_list import event_list, add_new_event
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
    return render_template("add_event.jinja", title = "Add Event")

@events_blueprint.route("/events", methods=["POST"])
def post_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    guest_capacity = request.form["guest capacity"]
    location = request.form["location"]
    description = request.form["description"]
    if 'recurring_checkbox' in request.form:
        event_recurring = True
    else: 
        event_recurring = False
    new_event = Event(event_date, event_name, guest_capacity, location, description, event_recurring)
    add_new_event(new_event)
    return render_template("events.jinja", event_list = event_list, title = "Events List")

@events_blueprint.route("/events/<index>/delete", methods=["get", "post"])
def delete_event(index):
    del event_list[int(index)]
    return render_template("events.jinja", event_list = event_list, title = "Events List")