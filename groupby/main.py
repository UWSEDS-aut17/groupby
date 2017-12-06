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
    data : list of lists
    
        data[0] : confirmation/error message for testing
    
        data[1] : list containing the data
        
            data[1][0] : pandas dataframe of tweets, error message, or None
            
            data[1][1] : list of pandas dataframes, error message, or None
                data[1][1][0] : pandas dataframe of LinkedIn connections
                data[1][1][1] : pandas dataframe of LinkedIn invitations
            
            data[1][2] : list of pandas dataframes, error message, or None
                data[1][2][0] : pandas dataframe of Facebook friends
                data[1][2][1] : pandas dataframe of Facebook timeline
            
            data[1][3] : icalendar.Calendar, error message, or None
    
    """
    
    tw = None
    li = None
    fb = None
    gcal = None
    
    for i, val in enumerate(user_args):
        
        if val == '-T':
            tw_path = user_args[i+1]
            tw_file = 'tweets.csv'
            tw_fname = tw_path + '/' + tw_file
            tw = groupby.twitter.open_tweets(tw_fname)
    
        if val == '-L':
            li_path = user_args[i+1]
            li_con_file = 'Connections.csv'
            li_con_fname = li_path + '/' + li_con_file
            con_df = groupby.linkedin.open_linkedin(li_con_fname)            
            li_invites_file = 'Invitations.csv'
            li_invites_fname = li_path + '/' + li_invites_file
            invites_df = groupby.linkedin.open_linkedin(li_invites_fname)
            li = [con_df, invites_df]

        if val == '-F':
            fb_path = user_args[i+1]
            fb_friends_file = 'html/friends.htm'
            fb_friends_fname = fb_path + '/' + fb_friends_file
            friends_df = groupby.facebook.open_friends(fb_friends_fname)
            fb_timeline_file = 'html/timeline.htm'
            fb_timeline_fname = fb_path + '/' + fb_timeline_file
            timeline_df = groupby.facebook.open_timeline(fb_timeline_fname)
            fb = [friends_df, timeline_df]
            
        if val == '-C':
            gcal_file = user_args[i+1]
            gcal = groupby.gcal.open_gcal(gcal_file)
            
    return ["File(s) loaded successfully", [tw, li, fb, gcal]]


def build_report(user_args, data):    
    r"""Build PDF report with data visualizations and tables.
    
    Parameters
    ----------
    data : list of lists
    
        data[0] : pandas dataframe of tweets, error message, or None
        
        data[1] : list of pandas dataframes, error message, or None
            data[1][0] : pandas dataframe of LinkedIn connections
            data[1][1] : pandas dataframe of LinkedIn invitations
            
        data[2] : list of pandas dataframes, error message, or None
            data[2][0] : pandas dataframe of Facebook friends
            data[2][1] : pandas dataframe of Facebook timeline
            
        data[3] : icalendar.Calendar, error message, or None
    
    """
    
    report_figures = []
        
    try:
        
        for i, val in enumerate(user_args):
            
            if val == '-T':

                tweets_df = data[0]
                unique_tweets, retweeted = groupby.twitter.tweet_explore(tweets_df)
                hashtags, hashtags_int, values = groupby.twitter.hashtag_clean(tweets_df)
                friends_list, friends_int, m_values = groupby.twitter.mentions_clean(tweets_df)
                month_df, labels = groupby.twitter.date_clean(tweets_df)

                tweets = ('Total number of unique tweets:', unique_tweets)
                retweets = ('Total retweeted tweets', retweeted)
                top_5_hashtags = groupby.plotters.plot(tweets, values, 
                                                        tweets_int, 'hashtags', 
                                                        'Number', 
                                                        'Top 5 Tweet Hashtags', 
                                                        (15,5), 'Green', '-T')
                top_mentions = groupby.plotters.plot(friends_list, m_values, 
                                                     friends_int, 'Friend', 
                                                     'Number of Mentions', 
                                                     'Top 5 Friend Mentions', 
                                                     (15,5) , 'Green', '-T')
                tweets_per_month = groupby.plotters.plot_tweetDate(month_df, 
                                                                   labels,
                                                                   'Month', 
                                                                   'Number of Tweets', 
                                                                    'Total Tweets Per Month', 
                                                                    (15,5) , 'Purple')
                
            if val == '-L':
                li = data[1]
        
            if val == '-F':
                fb = data[2]
                
                
            if val == '-C':
                gcal = data[3]
    except:
        return "Unable to generate report"

    #generate report
    
    """
    try:
                
        if li:
            
            con_df_by_week = groupby.linkedin.clean_df(con_df, 'Connected On')
            invites_sent, invites_received = groupby.get_sent_receive_invites(invites_df, 'Direction')
            invites_sent_by_week = groupby.clean_df(invites_sent, 'Sent At')
            invites_received_by_week = groupby.clean_df(invites_received, 'Sent At')
            
            
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
            
            
            # FACEBOOK TIMELINE

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

            # FACEBOOK FRIENDS
            
            year = clean_friends()
            plot(year, 'Year', 'Date', 'Year', 'New Friends count', 'Bar plot- New Friend count made Across the Years',
            (15,5), 'red')
            plt.show()

        if gcal:
            pass
    
    """

user_args = sys.argv

validate_args(user_args)

data = open_files(user_args)[1]

build_report(user_args, data)
# https://matplotlib.org/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages

