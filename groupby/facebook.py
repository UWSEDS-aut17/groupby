
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import calendar
import numpy as np
import seaborn as sns


def open_facebook(fname):
    """
    This function reads in the appropriate html file for timeline information
    """
    with open(fname) as f:
        soup = BeautifulSoup(f, "lxml")
    return soup
    
    
def open_timeline(fname):
    """
    Calls the read_facebook_timeline_data function, and then strips 
    data of all html tags. Once done this creates the information for 
    usage across days of the week, month of the year and year.
    """
    
    try:
        soup = open_facebook(fname)
    except:
        print("\n\n Please provide a valid path to your Facebook directory")
        return "Can't read Facebook data"
    
    try:
        timeline_info = soup.find_all("div", class_ = 'meta')
        clean_timeline = []
        for i in timeline_info:
            clean_timeline.append(re.sub(r'<.+?>', '', str(i)))
        clean_new_timeline = []
        for i in clean_timeline:
            clean_new_timeline.append([x.strip() for x in i.split(',')])
        days_information = [item[0] for item in clean_new_timeline]
        days = dict(Counter(days_information))
        list_of_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for k in list_of_days:
            if k not in days:
                days[k] = 0
            else:
                pass
        days = pd.DataFrame.from_dict(days, orient = 'index').reset_index().rename(columns = {'index': 'Days', 0:'Count'})
        date_information = [item[1] for item in clean_new_timeline]
        clean_new_date = []
        for i in date_information:
            clean_new_date.append([x.strip() for x in i.split('at')])
        date_information = [item[0] for item in clean_new_date]
        date = pd.DataFrame(np.array(date_information), columns= {'Date'})
        date['Date'] = pd.to_datetime(date['Date'])
        month = date['Date'].groupby([date.Date.dt.month]).agg('count')
        month = pd.DataFrame(month).rename(columns = {'Date': 'Count'}).reset_index()
        month['Date'] = month['Date'].apply(lambda x: calendar.month_abbr[x])
        year = date['Date'].groupby(date.Date.dt.year).agg('count')
        year = pd.DataFrame(year).rename(columns = {'Date': 'Count'}).reset_index()
        return days, month, year
    except:
        return "Unable to clean Facebook timeline data"


def open_friends(fname):
    """
    Calls the read_facebook_friends_data function, and then strips 
    data of all html tags. Once done this creates the information for 
    friends made across the years.
    
    """
    
    try:    
        soup = open_facebook(fname)
    except:
        print("\n\n Please provide a valid path to your Facebook directory")
        return "Can't read Facebook data"
   
    try:
        friends_info = soup.find_all('div', class_ = 'contents')
        clean_friends = []
        for i in friends_info:
            clean_friends.append(re.sub(r'<.+?>', '', str(i)))
        clean_new_timeline = []
        for i in clean_friends:
            clean_new_timeline.append([x.strip() for x in i.split('Sent Friend Requests')])
        temp = [item[0] for item in clean_new_timeline]
        clean = []
        for i in temp:
            clean.extend(re.findall('\(.*?\)',i))
        clean_new = []
        for i in clean:
            clean_new.append(i.strip('()'))
        the_new_list = [x.split(',') for x in clean_new]
        new =[]
        for l in range(len(the_new_list)):
            k = [x.split(' ') for x in the_new_list[l]]
            if len(k[0]) == 2:
                k[0].append('2017')
            new.append(k[0])
        clean_df = pd.DataFrame(new).rename(columns = {0:'Date', 1:'Month', 2:'Year'})
        year = clean_df.groupby('Year').agg('count')
        year = year.reset_index()
        return year
    except:
        return "Unable to clean Facebook friends data"
