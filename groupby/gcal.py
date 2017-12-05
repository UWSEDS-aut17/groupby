from icalendar import Calendar, Event
import pandas as pd


def open_gcal(fname):
    cal_file = open(fname, 'rb')
    try:
        gcal = Calendar.from_ical(cal_file.read())
        return gcal
    except:
        print("\n\n Please provide a valid path to your Google Calendar data (ICS file)")


def cal_to_df(data):
    
    cal_data = []
    for component in data.walk():
        if component.name == "VEVENT":
            dt_c = component.get('dtstart').dt
            cal_data.append(dt_c)
    cal_df = pd.DataFrame({'event_date':cal_data})            
    return cal_df

def events_per_week():
    pass

fname = 'data/shsher@uw.edu.ics'
cal_data = open_gcal(fname)
cal_to_df(cal_data)
