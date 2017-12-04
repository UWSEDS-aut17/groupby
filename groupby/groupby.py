"""
Description of script
"""


# check valid args

# check valid files

# get individual    
    
# LINKED IN
con_df = read_safely('./connections.csv')
con_df_by_week = clean_df(con_df, 'Connected On')
invites_df = read_safely('Invitations.csv')
invites_sent, invites_received = get_sent_receive_invites(invites_df, 'Direction')
invites_sent_by_week = clean_df(invites_sent, 'Sent At')
invites_received_by_week = clean_df(invites_received, 'Sent At')
plot(con_df_by_week,'Connected On','Email Address', 'Weeks', 
     'Number of Connections', 'Bar Plot - Number of Connections per week', 
     (15,5), 'purple')
plot(invites_sent_by_week,'Sent At','From', 'Weeks', 
     'Number of Invites', 'Bar Plot - Number of Invites Sent per week', 
     (15,5), 'green')
plot(invites_received_by_week,'Sent At','From', 'Weeks', 
     'Number of Invites', 'Bar Plot - Number of Invites Sent per week', 
     (15,5), 'red')
import_recruiters_contacts('Connections.csv')

# TWITTER
tweets_df = read_twitter()
unique_tweets,retweeted = tweet_explore(tweets_df)
hashtags, hashtags_int, values = hashtag_clean(tweets_df)
friends_list, friends_int, m_values = mentions_clean(tweets_df)
month_df, labels = date_clean(tweets_df)
print('Total number of unique tweets:', unique_tweets)
print('Total retweeted tweets', retweeted)
plot(tweets,values , tweets_int ,'hashtags' , 'Number' , 'Top 5 Tweet Hashtags', (15,5) , 'Green')
plt.show()
plot(friends_list,m_values , friends_int ,'Friend' , 'Number of Mentions' , 'Top 5 Friend Mentions', (15,5) , 'Green')
plt.show()
plot_tweetDate(month_df, labels ,'Month' , 'Number of Tweets' , 'Top Per Month', (15,5) , 'Purple')
plt.show()

# FACEBOOK
