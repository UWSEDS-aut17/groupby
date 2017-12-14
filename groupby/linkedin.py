import pandas as pd
import matplotlib.pyplot as plt
import datetime


def open_linkedin(fname):
    """
    Function to read linkedIn data and return a data DataFrame

    Parameters:
    -----------
    fname: LinkedIn csv file

    Returns:
    --------
    data : LinkedIn dataframe
    """

    try:
        data = pd.read_csv(fname, encoding = "ISO-8859-1")
        return data
    except:
        print("\n\n Please provide a valid path to your LinkedIn directory")
        return "Can't read LinkedIn data"


def clean_df(df, date_column):
    """
    Function to use linked in data frame, aggregare it by week and return a data frame

    Parameters:
    -----------
    df : LinkedIn DataFrame
    date_column : Name of date_column

    Returns:
    --------
    DataFrame
    df_by_week: LinkedIn data aggregated by week
    """

    df['count'] = 1
    df[date_column] = pd.to_datetime(df[date_column])
    df['date_minus_time'] = df[date_column].apply(
        lambda df: datetime.datetime(year=df.year, month=df.month, day=df.day))
    df.set_index(df["date_minus_time"], inplace=True)

    week_counts = df['count'].resample('W').sum()
    week_counts = week_counts.fillna(0)
    df_by_week = pd.DataFrame({date_column: week_counts.index, 'count': week_counts.values})
    return df_by_week


def get_sent_receive_invites(df, direction_column):

    """
    Function to return subsets of linkedIn data frame 
    With rows corresponding to invites sent and a second data frame with rows corresponding to invites invites_received

    Parameters:
    -----------
    df : LinkedIn DataFrame
    direction_column : INGOING or OUTGOING

    Returns:
    --------
    DataFrame
    invites_sent: LinkedIn data subset to include only connections sent rows
    invites_received: LinkedIn data subset to include only connections received rows
    """

    invites_sent = df[df[direction_column] == 'OUTGOING']
    invites_received = df[df[direction_column] == 'INCOMING']
    return invites_sent, invites_received


def import_recruiters_contacts(path):

    """
    Function to return the list of recruiters connected with, from the linkedIn dataset

    Parameters:
    -----------
    path: Path to LinkedIn file

    Returns:
    --------
    Dataframe
    recruiters_df: Dataframe consisting of list of recruiters along with their positions
    """

    contacts_df = open_linkedin(path)
    words = ['Recruiter', 'Talent', 'Sourcer', 'Recruiting']
    contacts_df['Position'] = contacts_df['Position'].dropna().apply(lambda x: 'Recruiter' if 
                                                   (any(word in x for word in words)) else x,1)
    recruiters_df = contacts_df[contacts_df['Position'] == 'Recruiter']
    return recruiters_df

def plot(df, x,y, xlabel, ylabel, title, fig_size, fig_color):

    """
    Functions to plot linkedIn figures

    Parameters
    ----------
    df : Facebook DataFrame
    x  : Data to plot on x-axis
    y  : Data to plot on y-axis
    xlabel : Label for x-axis
    ylabel : Label for y-axix
    title : Plot title
    fig_size : Size of output figure
    fig_color : Color for the bar chart

    Returns
    -------
    Figure object of line charts

    """
    
    fig,ax= plt.subplots(nrows=1)
    ax.plot(df[x],df[y], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.set_size_inches(fig_size)
    return fig