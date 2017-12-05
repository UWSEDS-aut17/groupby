from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone



"""
Decisions to make:

- Count or duration?
- Count or duration for all-day events?
- Overlapping all-day events??
"""


cal = Calendar()
gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        print(component.get('dtstart'))
        print(component.get('dtend'))
        print(component.get('dtstamp'))
g.close()