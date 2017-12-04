from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

cal = Calendar()
g = open('shsher@uw.edu.ics','rb')
gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        print(component.get('dtstart'))
        print(component.get('dtend'))
        print(component.get('dtstamp'))
g.close()