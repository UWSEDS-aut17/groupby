from icalendar import Calendar, Event
import pandas as pd
import matplotlib.pyplot as plt


def open_gcal(fname):
    """Opens Google Calendar ICS file.
    
    Parameters
    ----------
    fname : string
        the full path (including filename) of the Google Calendar data
    
    Returns
    -------
    gcal : icalendar.Calendar object
    
    """
    
    cal_file = open(fname, 'rb')
    
    try:
        gcal = Calendar.from_ical(cal_file.read())
        return gcal
    except:
        print("\n\n Please provide a valid path to your Google Calendar data "
            "(the actual ICS file)")


def cal_to_df(data):
    """Converts icalendar.Calendar object to pandas dataframe.
    
    Create dataframe with event_date, year, month, and day columns, where 
    each row represents an event. Each event is counted as occurring on the day 
    it began, i.e. multi-day events are counted only once.
    
    Parameters
    ----------
    data : icalendar.Calendar object
    
    Returns
    -------
    cal_df : pandas dataframe
    
    """
    
    cal_data = []
    for component in data.walk():
        if component.name == "VEVENT":
            dt_c = component.get('dtstart').dt
            cal_data.append(dt_c)
    cal_df = pd.DataFrame({'event_date':cal_data})  
    cal_df['year'] = pd.to_datetime(cal_df['event_date'], utc=True).dt.year
    cal_df['month'] = pd.to_datetime(cal_df['event_date'], utc=True).dt.month 
    cal_df['day'] = pd.to_datetime(cal_df['event_date'], utc=True).dt.day
    return cal_df


def events_per_month(cal_df):
    """Count total events per month.
    
    Parameters
    ----------
    cal_df : pandas dataframe
    
    Returns
    -------
    events_per_month : pandas series
        
    """
    
    events_per_month = cal_df.groupby(['year', 'month']).count()
    print(events_per_month)
    return events_per_month


def events_per_week(cal_df):
    cal_df['event_date'] = pd.to_datetime(cal_df['event_date'], utc=True).dt.date
    cal_df['event_date'] = cal_df['event_date'] - pd.to_timedelta(7, unit='d')
    events_per_week = cal_df.groupby(['event_date']).count().reset_index()
    print(events_per_week)
    return events_per_week


def plot_events(events):
    """Plot total events per month.
    
    Parameters
    ----------
    events_df : pandas series
        
    """
    pass


fname = 'data/shsher@uw.edu.ics'
cal_data = open_gcal(fname)
cal_df = cal_to_df(cal_data)
events = events_per_month(cal_df)
events_per_week(cal_df)
plot_events(events, 'Total Events')