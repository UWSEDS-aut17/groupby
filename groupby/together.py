
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from collections import Counter
import re
import matplotlib.dates as mdates
from bs4 import BeautifulSoup
import calendar


def make_month(df,date_column,flag):
    """
    Function to use a social media data frame and return a data frame of Year-Month and activity count
    """
    df['date'] = pd.to_datetime(df[date_column]).dt.date
    df['year'] = pd.to_datetime(df[date_column]).dt.year
    df['month'] = pd.to_datetime(df[date_column]).dt.month
    df_new = df[['date','year','month']]
    if flag == 'T':
        col = 'twitter-count'
    if flag == 'L':
        col = 'ln-count'
    if flag == 'F':
        col = 'fb-count'
    if flag == 'G':
        col = 'cal-count'
    df_new[col]=df_new['year'].apply(str)+'-'+df_new['month'].apply(str)
    df_new[col]=pd.DatetimeIndex(df_new[col],frequency = 'D')
    df_new = df_new[[col]]
    df_new = df_new[col].value_counts().reset_index()
    return df_new


def plot_crossds(joined_df):
    """
    Plots a line chart for overall activity across all social media platform
    """
    try:
        plt.style.use('seaborn-darkgrid')
        fig,ax= plt.subplots(nrows=1)
        ax.plot(joined_df['index'],joined_df['twitter-count'],label = 'Twitter Activity',color = '#1DA1F2',linewidth=2, alpha=0.7)
        ax.plot(joined_df['index'],joined_df['ln-count'], label = 'LinkedIn Activity',color = '#328332',linewidth=2, alpha=0.7)
        ax.plot(joined_df['index'],joined_df['fb-count'], label = 'Facebook Activity',color = '#3b5998',linewidth=2, alpha=0.7)
        ax.plot(joined_df['index'],joined_df['cal-count'], label = 'Calendar Activity',color = '#db3236',linewidth=2, alpha=0.7)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.legend(loc='upper right', prop={'size': 20})
        plt.yticks(fontsize=16,fontstyle='italic')
        plt.xticks(fontsize=16,fontstyle='italic')
        ax.set_xlabel('Year-Month',fontsize=18)
        ax.set_ylabel('Activity Count',fontsize=18)
        ax.set_title('Social Media Activity by Year-Month',fontsize=24,fontweight='bold')
        fig.set_size_inches(15,10)
        return fig
    except:
        return "Can't generate plot"
