"""This script 

"""



import sys
import pandas as pd
from icalendar import Calendar, Event


def validate_args(user_args):
    r"""Checking user-provided arguments for validity.
        
    Parameters
    ----------
    user_args : list of strings
        arguments passed from command line to script via sys.argv
        
    Returns
    -------
    msg : str or None
        error message
        
    """

    if len(user_args) < 3:
        print("\n\n Please indicate at least one social media dataset, " 
            "for example: \n\t python groupby.py -T path/Twitter_directory/")
        return "Failed to provide minimum argument"    

    options = user_args[1::2]
    soc_med = False
    
    for opt in options:
        if opt not in ['-T', '-F', '-L', '-C']:
            print("\n\n Please indicate valid options: \n\t -T, -F, -L, or -C")
            return "Wrong option provided (not -T, -F, -L or -C)"
        if opt in ['-T', '-F', '-L']:
            soc_med = True
  
    if soc_med == False:
        print("\n\n Please indicate at least one social media dataset, "
            "for example: \n\t python groupby.py -T path/Twitter_directory/")
        return "Failed to provide social media data" 
    
    if (len(user_args)-1) % 2 != 0:
        print("\n\n For every option (-T, -F, -L, -C), indicate a corresponding "
            "path, for example: \n\t python groupby.py -T path/here/")
        return "Incomplete option:argument pair"
    
    return None



def open_files(user_args):
    
    tweets_df = None
    con_df = None 
    invites_df = None 
    friends_df = None 
    timeline_df = None 
    ads_df = None 
    gcal = None

    for i, val in enumerate(user_args):
   
        if val == '-T':
            tw_path = user_args[i+1]
            tw_file = 'tweets.csv'
            try:
                tweets_df = pd.read_csv(tw_path + '/' + tw_file)
            except:
                print("\n\n Please provide a valid path to your Twitter directory")

            
        if val == '-L':
            li_path = user_args[i+1]
            li_connections_file = 'Connections.csv'
            li_invitations_file = 'Invitations.csv'
            try:
                con_df = pd.read_csv(li_path + '/' + li_connections_file, encoding = "ISO-8859-1")
                invites_df = pd.read_csv(li_path + '/' + li_invitations_file, encoding = "ISO-8859-1")
            except:
                print("\n\n Please provide a valid path to your LinkedIn directory")

        """
        if val == '-F':
            fb_path = user_args[i+1]
            fb_friends_file = 'html/friends.htm'
            fb_timeline_file = 'html/timeline.htm'
            fb_ads_file = 'html/ads.htm'
            try:
                friends_df = 
                timeline_df =
                ads_df =
            except:
                print("\n\n Please provide a valid path to your Facebook directory")
        """
        
        if val == '-C':
            cal_file = open(user_args[i+1], 'rb')
            try:
                gcal = Calendar.from_ical(cal_file.read())
            except:
                print("\n\n Please provide a valid path to your Google Calendar data (ICS file)")

    return [tweets_df, [con_df, invites_df], [friends_df, timeline_df, ads_df], gcal]


def analyze_data(data):
    
    tw = data[0]
    li = data[1]
    fb = data[2]
    cal = data[3]
    
    if tw:
        unique_tweets,retweeted = twitter.tweet_explore(tweets_df)
        hashtags, hashtags_int, values = twitter.hashtag_clean(tweets_df)
        friends_list, friends_int, m_values = twitter.mentions_clean(tweets_df)
        month_df, labels = twitter.date_clean(tweets_df)
        print('Total number of unique tweets:', unique_tweets)
        print('Total retweeted tweets', retweeted)
        plot(tweets, values, tweets_int, 'hashtags', 'Number', 'Top 5 Tweet Hashtags', (15,5) , 'Green')
        plt.show()
        plot(friends_list, m_values, friends_int, 'Friend', 'Number of Mentions', 'Top 5 Friend Mentions', (15,5) , 'Green')
        plt.show()
        plot_tweetDate(month_df, labels,'Month', 'Number of Tweets', 'Top Per Month', (15,5) , 'Purple')
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


user_args = sys.argv

validate_args(user_args)

data = open_files(user_args)

#analyze_data(data)

