unique_tweets,retweeted = tweet_explore(tweets_df)
hashtags, hashtags_int, values = hashtag_clean(tweets_df)
friends_list, friends_int, m_values = mentions_clean(tweets_df)
month_df, labels = date_clean(tweets_df)