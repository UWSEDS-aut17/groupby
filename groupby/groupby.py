"""
This script 
"""


import sys

#import facebook
#import linkedin
#import twitter
#import gcal


def validate_args(user_args):    

    if len (user_args) < 3:
        print("\n\n Please indicate at least one social media dataset, for example: \n\n\t python groupby.py -T path/Twitter_directory/")
        return 'Failed to provide minimum argument'          

    options = user_args[1::2]
    soc_med = False
    for opt in options:
        if opt not in ['-T', '-F', '-L', '-C']:
            print("\n\n Please indicate valid options: \n\n\t -T, -F, -L, or -C")
            return 'Wrong option provided (not -T, -F, -L or -C)'
        if opt in ['-T', '-F', '-L']:
            soc_med = True
    if soc_med == False:
        print("\n\n Please indicate at least one social media dataset, for example: \n\n\t python groupby.py -T path/Twitter_directory/")
        return 'Failed to provide social media data'          
    
    ## each option has an arg?
    if len(user_args)-1 % 2 != 0:
        print('\n\n Please make sure every option (-T, -F, -L, -C) has a corresponding path ')
        return('Incomplete option:argument pair')



"""
 
    # at least two arguments, the first of which indicates a social media dataset?
    if len(user_args) < 3 or user_args[1] not in ['-T', '-F', '-L']:
        print("\n\n Please indicate at least one social media dataset, for example: \n\n\t python groupby.py -T path/Twitter_directory/")
        return 'Failed to provide minimum argument'
"""

"""


def open_files(user_args):

    for i in len(user_args)-1:
        
        # Twitter
        if user_args[i] == '-T':       
            tw_path = user_args[i+1]
            tw_file = 'tweets.csv'
            try:
                tweets_df = read_twitter(tw_path + tw_file)
            except:
                tw = False
                print("Please provide a valid path to your Twitter directory")
            else:
                tw = True
        
        
                # Facebook
        if user_args[i] == '-F':
            fb_path = user_args[i+1]
            fb_friends_file = 'html/friends.htm'
            fb_timeline_file = 'html/timeline.htm'
            fb_ads_file = 'html/ads.htm'
            try:
                fb = open()
            except:
                fb = False
                print("Please provide a valid path to your Facebook directory")
            else:
                fb = True
        
        # LinkedIn
        if user_args[i] == '-L':
            li_path = user_args[i+1]
            li_connections_file = 'connections.csv'
            li_invitations_file = 'Invitations.csv'
            try:
                con_df = linkedin.read_safely(li_path + li_connections_file)
                invites_df = linkedin.read_safely(li_path + li_invitations_file)
            except:
                li = False
                print("Please provide a valid path to your LinkedIn directory")  
            else:
                li = True

        if user_args[i] == '-C':
            cal_file = user_args[i+1]
            try:
                g = open('shsher@uw.edu.ics','rb')
            except:
                cal = False
                print("Please provide a valid path to your Google Calendar data (ICS file)")  
            else:
                cal = True


if tw:
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
        
if li:
    con_df_by_week = linkedin.clean_df(con_df, 'Connected On')
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

if fb:
    pass

if cal:
    pass
"""


user_args = sys.argv

validate_args(user_args)

#open_files(user_args)

