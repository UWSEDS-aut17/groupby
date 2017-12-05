import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from collections import Counter


def open_tweets(fname):
    try:
        tweets_df = pd.read_csv(fname)
    except:
        print("\n\n Please provide a valid path to your Twitter directory")


def tweet_explore(tweets_df):
    unique_tweets = tweets_df.tweet_id.nunique()
    retweeted = tweets_df.retweeted_status_id.nunique()
    return unique_tweets,retweeted


def date_clean(tweets_df):

    tweets_df['month'] = pd.to_datetime(tweets_df['timestamp']).dt.month
    tweets_per_month = tweets_df.groupby(['month'])['tweet_id'].count().reset_index()
    labels = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep' , 'Oct', 'Nov', 'Dec']
    return tweets_per_month , labels

def hashtag_clean(tweets_df):
    hashtags = tweets_df.text.str.findall(r'#.*?(?=\s|$)')
    _hashtags_list = []
    tweets_int = []
    tweets = []
    values = []
    for i in range(0,len(hashtags)):
        if len(hashtags[i]) != 0:
            _hashtags_list.append(hashtags[i])
            
    hashtags_list = [item for sublist in _hashtags_list for item in sublist]
    hashtag_dict = Counter(hashtags_list)

    for k, v in sorted(hashtag_dict.items(), key=lambda x: x[1], reverse=True):
        tweets.append(k)
        values.append(v)
        
    for i in range(0,len(tweets)):
        tweets_int.append(i)
        
    return tweets, tweets_int,values


def mentions_clean(tweets_df):
    friends = tweets_df.text.str.findall(r'@.*?(?=\s|$)')
    _friends_list = []
    for i in range(0,len(friends)):
        if len(friends[i]) != 0:
            _friends_list.append(friends[i])

    friends_list = [item for sublist in _friends_list for item in sublist]
    friends_dict = Counter(friends_list)
    mentions = []
    m_values = []
    for k, v in sorted(friends_dict.items(), key=lambda x: x[1], reverse=True):
        mentions.append(k)
        m_values.append(v)
    friends_int = []
    
    for i in range(0,len(friends_list)):
        friends_int.append(i)
        
    return friends_list, friends_int,m_values


def plot(x,y,z, xlabel, ylabel, title, fig_size, fig_color):
    fig,ax= plt.subplots(nrows=1)
    ax.bar(z[0:5],y[0:5], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(z[0:5], x[0:5])
    fig.set_size_inches(fig_size)
    return


def plot_tweetDate(x,y, xlabel, ylabel, title, fig_size, fig_color):
    fig,ax= plt.subplots(nrows=1)
    ax.bar(x['month'],x['tweet_id'], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(x['month'], y)
    fig.set_size_inches(fig_size)
    return
