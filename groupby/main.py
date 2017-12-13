"""python main.py -T data

"""


import argparse
from datetime import datetime
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os
import pandas as pd
import subprocess
import sys

import facebook
import gcal
import linkedin
import plotters
import twitter


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
            "corresponding path or filename, as appropriate. For example: "
            "\n\t python groupby.py -T path/here/")
        return "Incomplete option:argument pair"
    
    return



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
                fb_friends_fname = fb_path + '/' + fb_friends_file
                friends_df = facebook.open_friends(fb_friends_fname)
                print(len(friends_df))
                print(type(friends_df))
                fb_timeline_file = 'html/timeline.htm'
                fb_timeline_fname = fb_path + '/' + fb_timeline_file
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

    try:
        pdf = FPDF('P', 'in', 'Letter')
            
        if user_args.twitter is not None:

            pdf.add_page()
            pdf.set_margins(1, 1)
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=1, txt="Twitter", align='C', ln=1)
            
            tw_file = user_args.twitter
            tw_fname = cwd + '/' + data + '/' + tw_file
            tw = twitter.open_tweets(tw_fname)
            tweets_df = tw

            unique_tweets, retweeted = twitter.tweet_explore(tweets_df)
            tweets = "Total number of unique tweets: {}".format(unique_tweets)
            retweets = "Total retweeted tweets: {}".format(retweeted)
            pdf.set_font('Arial', '', 12)
            pdf.cell(w=0, h=.3, txt=tweets, ln=1)
            pdf.cell(w=0, h=.3, txt=retweets, ln=1)

            hashtags, hashtags_int, values = twitter.hashtag_clean(tweets_df)
            top_5_hashtags = plotters.plot(hashtags, values, hashtags_int, 'hashtags', 'Number', 'Top 5 Tweet Hashtags', (15, 5), 'Green', '-T')
            top_5_hashtags.savefig('top_5_hashtags.png')
            pdf.image('top_5_hashtags.png', w=7)
            subprocess.call(['rm', 'top_5_hashtags.png'])

            friends_list, friends_int, m_values = twitter.mentions_clean(tweets_df)
            top_mentions = plotters.plot(friends_list, m_values, friends_int, 'Friend', 'Number of Mentions', 'Top 5 Friend Mentions', (15, 5), 'Green', '-T')
            top_mentions.savefig('top_mentions.png')
            pdf.image('top_mentions.png', w=7)
            subprocess.call(['rm', 'top_mentions.png'])

            month_df, labels = twitter.date_clean(tweets_df)
            tweets_per_month = plotters.plot_tweetDate(month_df, labels, 'Month', 'Number of Tweets', 'Total Tweets Per Month', (15, 5), 'Purple')
            tweets_per_month.savefig('tweets_per_month.png')
            pdf.image('tweets_per_month.png', w=7)
            subprocess.call(['rm', 'tweets_per_month.png'])

            tweet_wordcloud = plotters.plot_wc(hashtags)
            tweet_wordcloud.savefig('tweet_wordcloud.png')
            pdf.add_page('L')
            pdf.set_margins(0, 0)
            pdf.image('tweet_wordcloud.png', w=18, x=-3.5, y=1)
            subprocess.call(['rm', 'tweet_wordcloud.png'])

            scores_dict = twitter.sentiment_dict('data/AFINN-111.txt')
            sentiments = twitter.tweet_score(tweets,scores_dict,tweets_df)
            sent_plot = plotters.plot_sentiment(sentiments)
            sent_plot.savefig('sent_plot.png')
            pdf.add_page('P')
            pdf.set_margins(1, 1)
            pdf.cell(w=0, h=.3, txt='', align='C', ln=1)
            pdf.image('sent_plot.png', w=7)
            subprocess.call(['rm', 'sent_plot.png'])
            
        if user_args.linkedin is not None:
                        
            pdf.add_page()
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=0.5, txt="LinkedIn", align='C', ln=1)
                        
            li_path = user_args.linkedin
            li_con_file = 'Connections.csv'
            li_con_fname = li_path + '/' + li_con_file
            li_invites_file = 'Invitations.csv'
            li_invites_fname = li_path + '/' + li_invites_file

            con_df = linkedin.open_linkedin(li_con_fname)
            con_df_by_week = linkedin.clean_df(con_df, 'Connected On')
            invites_df = linkedin.open_linkedin(li_invites_fname)

            connections = linkedin.plot(con_df_by_week, 'Connected On', 'count', 'Weeks', 'Number of Connections', 'Number of Connections per week', (15, 5), '#8D6CAB')
            connections.savefig('connections.png')
            pdf.image('connections.png', w=8.5, x=0)
            subprocess.call(['rm', 'connections.png'])

            invites_sent, invites_received = linkedin.get_sent_receive_invites(invites_df, 'Direction')
            invites_sent_by_week = linkedin.clean_df(invites_sent, 'Sent At')
            inv_sent = linkedin.plot(invites_sent_by_week, 'Sent At', 'count', 'Weeks', 'Number of Invites', 'Number of Invites Sent per week', (15, 5), '#8D6CAB')
            inv_sent.savefig('inv_sent.png')
            pdf.image('inv_sent.png', w=8.5, x=0)
            subprocess.call(['rm', 'inv_sent.png'])

            invites_received_by_week = linkedin.clean_df(invites_received, 'Sent At')
            inv_rec = linkedin.plot(invites_received_by_week, 'Sent At', 'count', 'Weeks', 'Number of Invites', 'Number of Invites Received per week', (15, 5), '#8D6CAB')
            inv_rec.savefig('inv_rec.png')
            pdf.image('inv_rec.png', w=8.5, x=0)
            subprocess.call(['rm', 'inv_rec.png'])
            
        
        if user_args.facebook is not None:
 
            pdf.add_page()
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=0.5, txt="Facebook", align='C', ln=1)
        
            fb_path = user_args.facebook
            fb_friends_file = 'html/friends.htm'
            fb_friends_fname = fb_path + '/' + fb_friends_file
            fb_timeline_file = 'html/timeline.htm'
            fb_timeline_fname = fb_path + '/' + fb_timeline_file
 
            friends_df = facebook.clean_friends(fb_friends_fname)
 
            days,month, year = facebook.clean_timeline(fb_timeline_fname)    
                
            activity_per_day = facebook.plot(days, 'Days', 'Count', 'Day Of Week', 'Timeline Count', 'Bar plot', (15,5), 'purple')
            activity_per_day.savefig('activity_per_day.png')
            pdf.image('activity_per_day.png', w=7, x=0)
            subprocess.call(['rm', 'activity_per_day.png'])

            activity_per_month = facebook.plot(month, 'Date', 'Count', 'Month', 'Activity count across months', 'Bar plot', (15,5), 'blue')
            activity_per_month.savefig('activity_per_month.png')
            pdf.image('activity_per_month.png', w=7, x=0)
            subprocess.call(['rm', 'activity_per_month.png'])
            
            activity_per_year = facebook.plot(year, 'Date', 'Count', 'Year', 'Activity count', 'Bar plot- Activity Across the Years', (15,5), 'red')
            activity_per_year.savefig('activity_per_year.png')
            pdf.image('activity_per_year.png', w=7, x=0)
            subprocess.call(['rm', 'activity_per_year.png'])
                        
            friends_per_year = facebook.plot(friends_df, 'Year', 'Date', 'Year', 'New Friends count', 'Bar plot- New Friend count made Across the Years', (15,5), 'red')
            friends_per_year.savefig('friends_per_year.png')
            pdf.image('friends_per_year.png', w=7, x=0)
            subprocess.call(['rm', 'friends_per_year.png'])
        

        if user_args.calendar is not None:
            pdf.add_page()
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=0.5, txt="Calendar", align='C', ln=1)
            
            calendar_file = user_args.calendar
            time_per_month, events_per_month, total_events = gcal.get_plots(calendar_file)
            #fig_list = gcal.get_plots(calendar_file)
            
            #for fig in fig_list:
                #fig.savefig('temp.png')
                #pdf.image('temp.png', w=8.5, x=0)
                #subprocess.call(['rm', 'temp.png'])
               
            time_per_month.savefig('time_per_month.png')
            pdf.image('time_per_month.png', w=8.5, x=0)
            subprocess.call(['rm', 'time_per_month.png'])

            events_per_month.savefig('events_per_month.png')
            pdf.image('events_per_month.png', w=8.5, x=0)
            subprocess.call(['rm', 'events_per_month.png'])

            total_events.savefig('total_events.png')
            pdf.image('total_events.png', w=6, x=0.3)
            subprocess.call(['rm', 'total_events.png'])
        
        
        # generate combined plot
        

        pdf.output('report.pdf', 'F')
        return "Report generated successfully"
    
    except:        
        print(sys.exc_info()[0])
        return "Unable to generate report"



def main():
    parser = argparse.ArgumentParser(
        description='Analyzes social media events to track time spent on activities.')
    parser.add_argument('-T',
                        '--twitter',
                        help=('The directory for Twitter data')
                        )
    parser.add_argument('-L',
                        '--linkedin',
                        help=('The directory for LinkedIn data')
                        )
    parser.add_argument('-F',
                        '--facebook',
                        help=('The directory for Facebook data')
                        #type=argparse.FileType('r', encoding='iso-8859-1')
                       )
    parser.add_argument('-C',
                        '--calendar',
                        help=('The Google Calendar file (.ics)')
                        )

    args = parser.parse_args()
    print(args)
    return build_report(args, 'data')
                        # .twitter,
                        #      args.linkedin,
                        #      args.facebook,
                        #      args.calendar)

main()
