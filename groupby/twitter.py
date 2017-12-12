import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from collections import Counter
import re
import sys



def open_tweets(fname):
    try:
        tweets_df = pd.read_csv(fname)
        return tweets_df
    except:
        print("\n\n Please provide a valid path to your Twitter directory")
        return "Can't read Twitter data"



def tweet_explore(tweets_df):
    unique_tweets = tweets_df.tweet_id.nunique()
    retweeted = tweets_df.retweeted_status_id.nunique()
    return unique_tweets, retweeted



def date_clean(tweets_df):
    tweets_df['month'] = pd.to_datetime(tweets_df['timestamp']).dt.month
    tweets_per_month = tweets_df.groupby(['month'])['tweet_id'].count().reset_index()
    labels = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep' , 'Oct', 'Nov', 'Dec']
    return tweets_per_month, labels



def hashtag_clean(tweets_df):
    try:
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
        
        return tweets, tweets_int, values
    except:
        print("Can't clean hashtags")



def mentions_clean(tweets_df):
    
    try:
        friends = tweets_df.text.str.findall(r'@.*?(?=\s|$)')
        _friends_list = []
        for i in range(0, len(friends)):
            if len(friends[i]) != 0:
                _friends_list.append(friends[i])

        friends_list = [item for sublist in _friends_list for item in sublist]
        
        for i in range(0,len(friends_list)):
            friends_list[i] = re.sub('[^A-Za-z0-9]+', '', friends_list[i])
        
        friends_dict = Counter(friends_list)
        mentions = []
        m_values = []
        for k, v in sorted(friends_dict.items(), key=lambda x: x[1], reverse=True):
            mentions.append(k)
            m_values.append(v)
        friends_int = []
        
        for i in range(0, len(mentions)):
            friends_int.append(i)
            
        return mentions, friends_int, m_values
    
    except:
        print(sys.exc_info()[0])
        print("Can't clean mentions")

def sentiment_dict(fp):
    scores_dict = {}
    sf = open(fp)
    for line in sf:
        word,score = line.split("\t")
        scores_dict[word] = int(score)
    sf.close()
    return scores_dict

def tweet_score(tweets,scores_dict,tweets_df):
    tweets_df['year'] = pd.to_datetime(tweets_df['timestamp']).dt.year
    tweets = []

    for text in tweets_df['text']:
        tweets.append(text)

    final_score = []
    for line in tweets:
        tweet_score = 0
        for word in line.split():
            if word in scores_dict.keys():
                tweet_score += scores_dict[word]
        final_score.append(tweet_score)

    sentiment_df = pd.DataFrame(
    {'year': tweets_df['year'].values,
     'score': final_score,
    })

    sentiments = sentiment_df.groupby('year')['score'].mean().reset_index()
    sentiments['year'] = sentiments['year'].astype(int)

    return sentiments