import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime


def open_linkedin(fname):
    try:
        data = pd.read_csv(fname, encoding = "ISO-8859-1")
        return data
    except:
        print("\n\n Please provide a valid path to your LinkedIn directory")
        return "Can't read LinkedIn data"


def clean_df(df, date_column):
    df['count'] = 1
    df[date_column] = pd.to_datetime(df[date_column])
    df['date_minus_time'] = df[date_column].apply(
        lambda df: datetime.datetime(year=df.year, month=df.month, day=df.day))
    df.set_index(df["date_minus_time"], inplace=True)

    week_counts = df['count'].resample('W', how='sum')
    week_counts = week_counts.fillna(0)
    df_by_week = pd.DataFrame({date_column: week_counts.index, 'count': week_counts.values})
    return df_by_week


def get_sent_receive_invites(df, direction_column):
    invites_sent = df[df[direction_column] == 'OUTGOING']
    invites_received = df[df[direction_column] == 'INCOMING']
    return invites_sent, invites_received


def import_recruiters_contacts(path):
    contacts_df = open_linkedin('./connections.csv')
    words = ['Recruiter', 'Talent', 'Sourcer', 'Recruiting']
    contacts_df['Position'] = contacts_df['Position'].dropna().apply(lambda x: 'Recruiter' if 
                                                   (any(word in x for word in words)) else x,1)
    recruiters_df = contacts_df[contacts_df['Position'] == 'Recruiter']
    return recruiters_df

def plot(df, x,y, xlabel, ylabel, title, fig_size, fig_color):
    fig,ax= plt.subplots(nrows=1)
    ax.plot(df[x],df[y], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.set_size_inches(fig_size)
    return