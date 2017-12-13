"""So that the user need not specify a path to every file, we ask them to provide the location of the unzipped archives for their social media data. 
Respectively, the top level directory of each archive is named 'Twitter/', 'Facebook/', and 'LinkedIn' by default, but our program allows the user to rename them.
As the internal structure of the archives may change over time, this file maps from that top-level directory to our data files of interest. 
Variables from this script are used by main.py.
"""


linkedin_cons = + 'Connections.csv'
linkedin_invs = + 'Invitations.csv'

facebook_friends = + '/html/friends.htm'
facebook_timeline = + '/html/messages.htm'

twitter = + 'tweets.csv'