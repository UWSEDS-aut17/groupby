# Functional specification

<br>

## Problem statement

Enable social media users to gain insights about their social media use

<br>

## User profile

### Domain knowledge 

Our user is someone who uses social media and is therefore familiar with terms that are specific to each platform ("Likes", "Retweets", etc.).

### Tool access & knowledge

Our user ...
 
- ... uses a digital calendar that can export ICS files
- ... is comfortable navigating the interfaces of their Twitter, Facebook, LinkedIn, and calendar to export personal data
- ... is comfortable downloading a script from GitHub to their own computer
- ... is comfortable opening a shell and typing a few commands

<br>

## Elements of the problem statement

- **Summarize and aggregate individual data sources**
    - Understand formats and schemas of data exported from Facebook, Twitter, LinkedIn, Google Calendar
    - Identify meaningful summaries (e.g. total number of posts, wordcloud of hashtags, etc.) and aggregations (e.g. total Tweets per week) for each data source
- **Synthesize across data sources to answer questions**
    - Do the user's levels of activity across different social media platforms rise and fall together, or do they cycle between one platform or another?
    - What times of day do they tend to be most active on social media?
    - How does their social media activity compare with their other activities, for example, how often does social media activity overlap with scheduled events?

<br>

## Use cases

### Summarize Facebook data

_**Prerequisite:** User has downloaded their Facebook data and our script to the same directory, and has opened a Bash terminal there_

- **User:** Launches program, providing filename argument
- **Program:**
    - (if invalid arguments) Returns argument options
    - (if invalid file) Returns input requirements
    - (if valid file argument)
        - Parses HTML to extract items of interest
        - Outputs summary to file

### Summarize LinkedIn data

### Summarize Twitter data

### Summarize Google Calendar data

_**Prerequisite:** User has downloaded their Google Calendar data and our script to the same directory, and has opened a Bash terminal there_

- **User:** Launches program, providing filename argument
- **Program:**
    - (if invalid arguments) Returns argument options
    - (if invalid file) Returns input requirements
    - (if valid file argument)
        - Parses ICS file to extract items of interest
        - Calculates duration of events
            - Corrects for overlap between all-day events and scheduled events
        - Outputs summary to file
        
### Identify peak hours for social media activity in aggregate

### Compare temportal trends across different social media platforms

_**Prerequisite:** User has downloaded their Facebook and Twitter along with our script to the same directory, and has opened a Bash terminal there_

- **User:** Launches program, providing filename arguments
- **Program:**
    - (if invalid arguments) Returns argument options
    - (if invalid files) Returns input requirements
    - (if valid file arguments)
        - Parses JSON and HTML files to extract datetimes for events of interest
        - Aggregates activity by time of day
        - Outputs data visualization

### Compare social media activity with other activities
