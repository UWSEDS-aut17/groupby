"""This script 

"""



import sys
import groupby.twitter
import groupby.gcal
import groupby.linkedin
import groupby.facebook
import groupby.plotters


def validate_args(user_args):
    r"""Check user-provided arguments for validity.
        
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
        print("\n\n For every option (-T, -F, -L, -C), indicate a "
            "corresponding path, for example: "
            "\n\t python groupby.py -T path/here/")
        return "Incomplete option:argument pair"
    
    return None



def open_files(user_args):
    r"""Open files and save data.
    
    Parses the list of arguments provided by the user, calling other modules
    to open the files.
    
    Parameters
    ----------
    user_args : list of strings
        arguments passed from command line to script via sys.argv    
    
    Returns
    -------
    data : a list of lists
    
        data[0] : confirmation/error message for testing
    
        data[1] : list containing the data
        
            data[1][0] : pandas dataframe of tweets, or error message
            
            data[1][1] : list of pandas dataframes, or error message
                data[1][1][0] : pandas dataframe of LinkedIn connections
                data[1][1][1] : pandas dataframe of LinkedIn invitations
            
            data[1][2] : list of pandas dataframes, or error message
                data[1][2][0] : pandas dataframe of Facebook friends
                data[1][2][1] : pandas dataframe of Facebook timeline
            
            data[1][3] : icalendar.Calendar, or error message
    
    """
    
    tweets_df = None
    con_df = None 
    invites_df = None 
    friends_df = None 
    timeline_df = None 
    gcal = None

    for i, val in enumerate(user_args):
         
        if val == '-T':
            tw_path = user_args[i+1]
            tw_file = 'tweets.csv'
            tw_fname = tw_path + '/' + tw_file
            tweets_df = groupby.twitter.open_tweets(tw_fname)
      
        if val == '-L':
            li_path = user_args[i+1]
            li_con_file = 'Connections.csv'
            li_con_fname = li_path + '/' + li_con_file
            con_df = groupby.linkedin.open_linkedin(li_con_fname)            
            li_invites_file = 'Invitations.csv'
            li_invites_fname = li_path + '/' + li_invites_file
            invites_df = groupby.linkedin.open_linkedin(li_invites_fname)

        if val == '-F':
            fb_path = user_args[i+1]
            fb_friends_file = 'html/friends.htm'
            fb_friends_fname = fb_path + '/' + fb_friends_file
            friends_df = groupby.facebook.open_friends(fb_friends_fname)
            fb_timeline_file = 'html/timeline.htm'
            fb_timeline_fname = fb_path + '/' + fb_timeline_file
            timeline_df = groupby.facebook.open_timeline(fb_timeline_fname)
                    
        if val == '-C':
            gcal_file = user_args[i+1]
            gcal = groupby.gcal.open_gcal(gcal_file)
    
    tw = tweets_df
    li = [con_df, invites_df] 
    fb = [friends_df, timeline_df]
    data = ["File(s) loaded successfully", [tw, li, fb, gcal]]
    
    return data


def build_report(data):    
    
    tw = data[0]
    li = data[1]
    fb = data[2]
    cal = data[3]
    
    report_figures = []
    
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
        
        recruiters_df = import_recruiters_contacts('Connections.csv')

    if fb:
        
        """
        FACEBOOK TIMELINE

        days, month, year = clean_timeline(fname)

        plot(days, 'Days', 'Count', 'Day Of Week', 'Timeline Count', 
            'Bar plot', (15,5), 'purple')
        plt.show()

        plot(days, 'Days', 'Count', 'Day Of Week', 'Timeline Count', 
            'Bar plot', (15,5), 'purple')

        plt.show()

        plot(month, 'Date', 'Count', 'Month', 'Activity count across months', 'Bar plot',
                (15,5), 'blue')
        plt.show()

        plot(year, 'Date', 'Count', 'Year', 'Activity count', 'Bar plot- Activity Across the Years',
                (15,5), 'red')
        plt.show()

        """
        
        """ FACEBOOK FRIENDS
        year = clean_friends()
        plot(year, 'Year', 'Date', 'Year', 'New Friends count', 'Bar plot- New Friend count made Across the Years',
        (15,5), 'red')
        plt.show()

        """

        pass

    if cal:
        pass


user_args = sys.argv

validate_args(user_args)

data = open_files(user_args)[1]

#build_report(data)
# https://matplotlib.org/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages

