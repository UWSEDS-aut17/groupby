
import argparse
from fpdf import FPDF
import pandas as pd
import subprocess
import sys

import groupby.facebook as facebook
import groupby.gcal as gcal
import groupby.linkedin as linkedin
import groupby.plotters as plotters
import groupby.together as together
import groupby.twitter as twitter

pd.options.mode.chained_assignment = None


def build_report(user_args):    
    r"""Build PDF report with data visualizations and tables.
    
    Parameters
    ----------
    
    """

    try:
        pdf = FPDF('P', 'in', 'Letter')
                        
        if user_args.linkedin is not None:

            print("Processing LinkedIn data...")
                        
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
            
            print("LinkedIn data processed successfully")

        if user_args.twitter is not None:

            print("Processing Twitter data...")

            pdf.add_page()
            pdf.set_margins(1, 1)
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=1, txt="Twitter", align='C', ln=1)
                        
            tw_path = user_args.twitter
            tw_file = "tweets.csv"
            tw_fname = tw_path + '/' + tw_file
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
            
            scores_dict = twitter.sentiment_dict('./groupby/data/AFINN-111.txt')
            sentiments = twitter.tweet_score(tweets, scores_dict, tweets_df)
            sent_plot = plotters.plot_sentiment(sentiments)
            sent_plot.savefig('sent_plot.png')
            pdf.add_page('P')
            pdf.set_margins(1, 1)
            pdf.cell(w=0, h=.3, txt='', align='C', ln=1)
            pdf.image('sent_plot.png', w=7)
            subprocess.call(['rm', 'sent_plot.png'])
            
            print("Twitter data processed successfully")
        
        if user_args.facebook is not None:
 
            print("Processing Facebook data...")
 
            pdf.add_page()
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=0.5, txt="Facebook", align='C', ln=1)
        
            fb_path = user_args.facebook
            fb_friends_file = 'html/friends.htm'
            fb_friends_fname = fb_path + '/' + fb_friends_file
            fb_timeline_file = 'html/timeline.htm'
            fb_timeline_fname = fb_path + '/' + fb_timeline_file
 
            friends_df = facebook.clean_friends(fb_friends_fname)
 
            days, month, year, fb_df = facebook.clean_timeline(fb_timeline_fname)    
                
            activity_per_day = facebook.plot(days, 'Days', 'Count', 'Day Of Week', 'Activity count', 'Timeline Activity Across Days', (15,5), 'purple')
            activity_per_day.savefig('activity_per_day.png')
            pdf.image('activity_per_day.png', w=8.5, x=0)
            subprocess.call(['rm', 'activity_per_day.png'])

            activity_per_month = facebook.plot(month, 'Date', 'Count', 'Month', 'Activity count', 'Timeline Actvity Across Months', (15,5), 'blue')
            activity_per_month.savefig('activity_per_month.png')
            pdf.image('activity_per_month.png', w=8.5, x=0)
            subprocess.call(['rm', 'activity_per_month.png'])
            
            activity_per_year = facebook.plot(year, 'Date', 'Count', 'Year', 'Activity count', 'Timeline Activity Across the Years', (15,5), 'red')
            activity_per_year.savefig('activity_per_year.png')
            pdf.image('activity_per_year.png', w=8.5, x=0)
            subprocess.call(['rm', 'activity_per_year.png'])
                        
            pdf.add_page('P')
            pdf.set_margins(1, 1)
            pdf.cell(w=0, h=.3, txt='', align='C', ln=1)
            friends_per_year = facebook.plot(friends_df, 'Year', 'Date', 'Year', 'New friends count', 'New Friends By Year', (15,5), 'red')
            friends_per_year.savefig('friends_per_year.png')
            pdf.image('friends_per_year.png', w=8.5, x=0)
            subprocess.call(['rm', 'friends_per_year.png'])

            print("Facebook data processed successfully")
        
        if user_args.calendar is not None:
            
            print("Processing calendar data...")
            
            pdf.add_page()
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=0.5, txt="Calendar", align='C', ln=1)
            
            calendar_file = user_args.calendar
            cal_df = gcal._process_calendar(calendar_file)
            time_per_month, events_per_month, total_events = gcal.get_plots(cal_df)
            cal_dates = gcal.get_cal_dates(cal_df)
               
            time_per_month.savefig('time_per_month.png')
            pdf.image('time_per_month.png', w=8.5, x=0)
            subprocess.call(['rm', 'time_per_month.png'])

            events_per_month.savefig('events_per_month.png')
            pdf.image('events_per_month.png', w=8.5, x=0)
            subprocess.call(['rm', 'events_per_month.png'])

            total_events.savefig('total_events.png')
            pdf.image('total_events.png', w=6, x=0.3)
            subprocess.call(['rm', 'total_events.png'])
        
            print("Calendar data processed successfully")

        if user_args.twitter and user_args.facebook and user_args.linkedin:
            pdf.add_page('L')
            pdf.set_margins(1, 1)
            pdf.set_font('Arial', 'B', 20)
            pdf.cell(w=0, h=0.5, txt="Summary", align='C', ln=1)            
            
            tweets_df_month = together.make_month(tweets_df, 'timestamp', 'T')
            fb_df_month = together.make_month(fb_df, 'Date', 'F')
            conn_df_month = together.make_month(con_df, 'Connected On', 'L')
            cal_df_new = gcal.get_cal_dates(cal_df)
            gcal_df_month = together.make_month(cal_df_new, 'Date', 'G')
            joined_df = tweets_df_month.merge(conn_df_month, left_on='index', right_on='index', how='outer').merge(gcal_df_month, left_on='index', right_on='index',
                                                                                                                   how='outer').merge(fb_df_month, left_on='index', right_on='index', how='outer').sort_values(by='index').fillna(0)
            all_together = together.plot_crossds(joined_df)
            all_together.savefig('all_together.png')
            pdf.image('all_together.png', w=9.5, h=6)
            subprocess.call(['rm', 'all_together.png'])

        pdf_loc = user_args.output + '/' + 'report.pdf'
        pdf.output(pdf_loc, 'F')
        print("Report generated successfully at {}".format(pdf_loc))
        return
    
    except:        
        print(sys.exc_info()[0])
        print("Unable to generate report")
        return



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
                       )
    parser.add_argument('-C',
                        '--calendar',
                        help=('The Google Calendar file (.ics)')
                        )

    parser.add_argument('-O',
                        '--output',
                        help=('The directory where the report should be located, e.g. ~/Desktop')
                        )

    args = parser.parse_args()
    return build_report(args)