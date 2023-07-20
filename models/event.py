class Event:

    def __init__(self, date, name, guest_capacity, location, description, event_recurring):
        self.date = date
        self.name = name
        self.guest_capacity = guest_capacity
        self.location = location
        self.description = description
        self.event_recurring = event_recurring