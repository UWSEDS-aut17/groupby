# Component design

<br>

## Component list

So that users can analyze their social media data as detailed in our use cases, we need the following components for each of our four datasets (Twitter, Facebook, LinkedIn, Google Calendar):

- **read_X_data()** - read each dataset into native data structures
- **summarize_X_data()** - calculate meaningful summary statistics and visualizations for X dataset
- **aggregate_X_data()** - aggregate selected activities for each dataset (# per day or # per week)
- **peak_hours()** and **time_use()** - compare and analyze the aggregated versions of our datasets
- **choose_report()** - handles command line-based interactions with user (displaying options, help messages, error messages, calling other functions to produce the desired report)

<br>

## Component specifications

### read_Facebook_data()

- **Description:** Facebook gives us multiple html files, that are parsed into python using beautifulsoup. From here we aim to give the user a snapshot of their facebook usage.

- **Inputs:**
  -***Friends.html*** - contains data about your list of friends, when you became friends with them, and the people you decided to terminate your friendship with. These are hidden in the 'div class = contents', and will be unwrapped into a pandas dataframe for information to display the social activeness since the inception of the user account.

  -***Timeline.html*** - contains data about the activity on the user's timeline / profile. Here the necessary information will be extracted from 'div class = 'meta' and 'div class = comment', fed into a pandas dataframe to show the activity of the user over time, and whether there are any specific months which see higher usage.

  -***Ads.html*** - information about the ads displayed to the user. Aim to analyze or display the list of ads that have been displayed to the user, and which organizations/ pages have contact information about the user.

-**Outputs:** - The outputs are the necessary dataframes needed for future / next functions, stripped of the html content. Summarize_facebook_data will perform further analysis.


### read_LinkedIn_data()

- **Description:** For LinkedIn, types of connections and invites sent/received are being analyzed. This will show what period was one most active in and their interaction with LinkedIn in terms of amount of time spent in networking per week.
- **Inputs:**
  - ***Connections.csv*** - contains data about LinkedIn connections, with the following features/columns:
    - First Name - Name
    - Last Name - Name
    - Position - Connection title/position
    - Company - Name of the company my connection works in
    - Connected_On - Date
  - ***Invitations.csv*** - contains data about invitations sent and received on LinkedIn, grouped by week with the following features/columns:
    - From - Invitation Sender's Name
    - To - Invitation Receiver's Name
    - Sent At - Date at which Invitation was sent/received.
    - Message - Message string
    - Direction - INCOMING / OUTGOING.
- **Outputs:** The ouputs are dataframes obtained by reading the input csv files, with the same features/columns.  

### read_Twitter_data()

- **Description:** We are analyzing trends in twitter usage to identify periods where the user is most active on the platform. We will also identify the top hashtags and mentions by the user during the selected date range.
- **Inputs:**
  - ***tweets.csv*** - contains data about tweets posted by the user, with the following features/columns:
    - tweet_id - Unique numeric identifier column for tweets
    - in_reply_to_status_id - Numeric identifier if user is responding to an existing tweet
    - in_reply_to_user_id - Numeric source tweet user id
    - timestamp - Tweet timing
    - text - The actual tweet
    - retweeted_status_id - Unique numeric id if retweeted, null otherwise
    - retweeted_status_user_id - Numeric ID of user who retweets
    - retweeted_status_timestamp - Time of retweet
    - expanded_urls - Contains any URLs posted with the tweet

    We will be loading the the above csv file, on to a pandas dataframe for subsequent analysis.
- **Outputs:** The ouput is a dataframes obtained by reading the input csv files, with the same features/columns.

### read_GCal_data()

- **Description:** _high level description of the roles of the component_
- **Inputs:** _be specific about the data types, e..g. for DataFrames, specify the column names and the types of the column values_
- **Outputs:** _same consideration as with inputs_

```
# psuedocode here
```

### summarize_X_data()

...

### aggregate_X_data()

...

### peak_hours()

- ... in aggregate
- ... broken down by platform

### time_use()

...

### choose_report()

...
