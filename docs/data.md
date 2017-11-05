# Data analysis

## Requirements

We need data sources that:

- are **structured;** 
- identify different **activities** across multiple social media platforms and the 'real world'; and
- are **timestamped.**

## Sources

Each source below is readily available to individual users, perhaps with a day or two lag as data is prepared for export---but our team has already obtained personal archives.

### Google Calendar

For each event, exported Google Calendar data includes the following (if populated by the user for a given event):

- Date of creation
- Duration
- Timestamp for beginning and end
- Description
- Location

### Twitter

For each tweet, exported Twitter data includes the following metadata alongside the actual text:

- Mentions, an indication of interaction with other users
- Replies, an indication of interaction with other users or a continuation of one's own line of thought
- Hashtags, an indication of key topics and participation in trends
- Location

### Facebook

Facebook data is structured as HTML, which we'll parse with `beautifulsoup` if we have time. This data includes:

- Shared posts and links
- Statuses
- New friendships
- Changes to or additions of profile information

### Other potential sources

- Instagram.com
- LinkedIn.com
- SnapChat.com

## Evaluation

| Dataset | Structure | Activities | Timestamp |
| --- | --- | --- | --- |
| Google Calendar | ICS | Without a lot of analysis, we can't disaggregate different types of activities in calendar data, but we can calculate the overall number of scheduled hours in a day (with special handling for overlapping and/or all-day events) | X |
| Twitter | JSON | Overall number of tweets; number of tweets featuring an interaction with another user, containing a URL, containing a hashtag, etc. | X |
| Facebook | HTML | Overall number of statuses, shared statuses, links, etc. | X |
