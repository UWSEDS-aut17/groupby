# Functional specification

## Problem statement

Enable social media users to gain insights about their social media use

## User profile

- **Domain knowledge:** Our user is someone who uses social media (Twitter and/or Facebook) and is therefore familiar with terms that are specific to each platform ("Likes", "Retweets", etc.).
- **Tool access & knowledge:** Our user ...
    - ... uses a digital calendar that can export ICS files
    - ... is comfortable navigating the interfaces of their Twitter, Facebook, LinkedIn, and calendar to export personal data
    - ... is comfortable downloading a script from GitHub to their own computer
    - ... is comfortable opening a shell and typing a few commands

## Elements of the problem statement

- **Summarize and/or aggregate individual data sources**
    - Understand formats and schemas of data exported from Facebook, Twitter, LinkedIn, Google Calendar
    - Identify meaningful summaries (e.g. total number of posts, wordcloud of hashtags, etc.) and aggregations (e.g. total Tweets per week) for each data source
- **Synthesize across data sources to answer questions**
    - Do the user's levels of activity across different social media platforms rise and fall together, or do they cycle between one platform or another?
    - What times of day do they tend to be most active on social media?
    - How does their social media activity compare with their other activities, for example, how often does social media activity overlap with scheduled events?

## Use cases

_Each use case should provide details about the interactions between the user and the system you are building. The responses provided by the user must be consistent with the user profile. For example, you should not expect a user who is a non-programmer to do python programming. A use case should specify a series of interactions between the user and the system to accomplish one of the elements of the problem statement. You should have at least 3 use cases._

### Summarize Facebook usage

**Prerequisite:** User has downloaded their Facebook data and our script to the same directory, and has opened a Bash terminal there

- **User:** Launches program, providing filename argument
- **Program:**
    - (if invalid arguments) Returns argument options
    - (if invalid file) Returns input requirements
    - (if valid file argument)
        - Parses HTML to extract items of interest
        - Outputs summary to file

### Summarize Google Calendar data

**Prerequisite:** User has downloaded their Google Calendar data and our script to the same directory, and has opened a Bash terminal there

- **User:** Launches program, providing filename argument
- **Program:**
    - (if invalid arguments) Returns argument options
    - (if invalid file) Returns input requirements
    - (if valid file argument)
        - Parses ICS file to extract items of interest
        - Calculates duration of events
            - Corrects for overlap between all-day events and scheduled events
        - Outputs summary to file

### Identify daily temporal patterns in social media use

**Prerequisite:** User has downloaded their Facebook and Twitter along with our script to the same directory, and has opened a Bash terminal there

- **User:** Launches program, providing filename arguments
- **Program:**
    - (if invalid arguments) Returns argument options
    - (if invalid files) Returns input requirements
    - (if valid file arguments)
        - Parses JSON and HTML files to extract datetimes for events of interest
        - Aggregates activity by time of day
        - Outputs data visualization
