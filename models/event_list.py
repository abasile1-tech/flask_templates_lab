from models.event import Event
import datetime

josh_birthday = Event(datetime.date(2023, 11, 28), "Josh's Birthday", 30, "Josh's House", "Josh's big birthday party extravaganza", True)
hogmanay = Event(datetime.date(2023, 12, 31), "Hogmanay", 100, "Princes Street", "Hogmanay Street Party", True)
halloween = Event(datetime.date(2023, 10, 31), "Halloween", 30, "Edinburgh Castle", "Halloween party at the castle", False)

event_list = [josh_birthday, hogmanay, halloween]

def add_new_event(event):
    event_list.append(event)