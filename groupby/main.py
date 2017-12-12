"""python main.py -T data

"""



import sys
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime
import twitter
import gcal
import linkedin
import facebook
import plotters
import argparse
import pandas as pd

cwd = os.getcwd()


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
            
        data[3] : list of Booleans
            data[3][0] : True if Twitter data opened successfully
            data[3][1] : True if LinkedIn data opened successfully
            data[3][2] : True if Facebook data opened successfully
            data[3][3] : True if Google Calendar data opened successfully
    
    """
    
    status = [False, False, False, False]
    tw = None
    li = None
    fb = None
    gcal = None
    
    try:
    
        for i, val in enumerate(user_args):
            
            if val == '-T':
                tw_path = user_args[i+1]
                tw_file = 'tweets.csv'
                tw_fname = cwd + '/' + tw_path + '/' + tw_file
                tw = twitter.open_tweets(tw_fname)
                #if tw != "Can't read Twitter data":
                    #status[0] = True

            if val == '-L':
                li_path = user_args[i+1]
                li_con_file = 'Connections.csv'
                li_con_fname = cwd + '/' + li_path + '/' + li_con_file
                con_df = linkedin.open_linkedin(li_con_fname)            
                li_invites_file = 'Invitations.csv'
                li_invites_fname = cwd + '/' + li_path + '/' + li_invites_file
                invites_df = linkedin.open_linkedin(li_invites_fname)
                li = [con_df, invites_df]
                #if li[0] != "Can't read LinkedIn data":
                    #status[1] = True

            if val == '-F':
                fb_path = user_args[i+1]
                fb_friends_file = 'html/friends.htm'
                fb_friends_fname = cwd + '/' + fb_path + '/' + fb_friends_file
                friends_df = facebook.open_friends(fb_friends_fname)
                fb_timeline_file = 'html/timeline.htm'
                fb_timeline_fname = cwd + '/' + fb_path + '/' + fb_timeline_file
                timeline_df = facebook.open_timeline(fb_timeline_fname)
                fb = [friends_df, timeline_df]
                #if fb[0] != "Can't read Facebook data":
                    #status[2] = True
                
            if val == '-C':
                gcal_file = user_args[i+1]
                gcal = gcal.open_gcal(gcal_file)
                #if gcal != "Can't read Google Calendar data":
                    #status[3] = True
                
        return ["File(s) loaded successfully", [tw, li, fb, gcal], status]
    
    except:
        return "Unable to load file(s)"



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
    print(user_args,data)
    try:
        pdf = PdfPages('report.pdf')
        # for i, val in enumerate(user_args):
        #     print(val)
        if user_args.twitter is not None :
            tw_file = user_args.twitter
            tw_fname = cwd + '/' + data + '/' + tw_file
            tw = twitter.open_tweets(tw_fname)
            tweets_df = tw

            unique_tweets, retweeted = twitter.tweet_explore(tweets_df)
            tweets = ('Total number of unique tweets:', unique_tweets)
            retweets = ('Total retweeted tweets', retweeted)

            hashtags, hashtags_int, values = twitter.hashtag_clean(tweets_df)
            top_5_hashtags = plotters.plot(hashtags, values, hashtags_int, 'hashtags', 'Number', 'Top 5 Tweet Hashtags',
                                           (15, 5), 'Green', '-T')
            print(top_5_hashtags)

            friends_list, friends_int, m_values = twitter.mentions_clean(tweets_df)
            top_mentions = plotters.plot(friends_list, m_values, friends_int, 'Friend', 'Number of Mentions',
                                         'Top 5 Friend Mentions', (15, 5), 'Green', '-T')
            print(top_mentions)

            month_df, labels = twitter.date_clean(tweets_df)
            tweets_per_month = plotters.plot_tweetDate(month_df, labels, 'Month', 'Number of Tweets',
                                                       'Total Tweets Per Month', (15, 5), 'Purple')
            print(tweets_per_month)

            wc = plotters.plot_wc(hashtags)

            scores_dict = twitter.sentiment_dict('AFINN-111.txt')
            sentiments = twitter.tweet_score(tweets,scores_dict,tweets_df)
            sent_plot = plotters.plot_sentiment(sentiments)

            # with PdfPages('report-{}.pdf'.format(datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))) as pdf:

            pdf.savefig(top_5_hashtags)
            pdf.savefig(top_mentions)
            pdf.savefig(tweets_per_month)
            pdf.savefig(wc)
            pdf.savefig(sent_plot)
            
            """
            pdf.attach_note(plt.text(retweets))
            pdf.attach_note(tweets)

            """

        if user_args.linkedin is not None:
            li = data[1]

        if user_args.facebook is not None:
            fb = data[2]

        if user_args.calendar is not None:
            calendar_file = user_args.calendar
            print(calendar_file)
            fig_list = gcal.get_plots(calendar_file)
            for fig in fig_list:
                pdf.savefig(fig)


        pdf.close()


                
        return "Report generated successfully"
    
    except:        
        print(sys.exc_info()[0])
        return "Unable to generate report"
   
    """
    try:
                
        if li:
            
            con_df_by_week = linkedin.clean_df(con_df, 'Connected On')
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



# user_args = sys.argv
# validate_args(user_args)
# data = open_files(user_args)[1]
# print(build_report(user_args, data))

# https://matplotlib.org/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages
# https://sukhbinder.wordpress.com/2015/09/09/pdf-with-matplotlib/

def main():
    parser = argparse.ArgumentParser(
        description='Analyzes social media events to track time spent on activities.')
    parser.add_argument('-T',
                        '--twitter',
                        help=('The directory for twitter data')
                        )
    parser.add_argument('-L',
                        '--linkedin',
                        help=('The directory for linkedin data')
                        )
    parser.add_argument('-F',
                        '--facebook',
                        help='the calendar file (.ics)'
                        #type=argparse.FileType('r', encoding='iso-8859-1'),
                       )
    parser.add_argument('-C',
                        '--calendar',
                        help=('the path containing calendar files')
                        )


    args = parser.parse_args()
    print(args)
    return build_report(args,'data')
                        # .twitter,
                        #      args.linkedin,
                        #      args.facebook,
                        #      args.calendar)

main()
