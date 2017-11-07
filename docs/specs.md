# Functional specification

## Problem statement

Enable social media users to gain insights about their social media use

## User profile

- **Domain knowledge:** Our user is someone who uses social media (Twitter and/or Facebook) and is therefore familiar with terms that are specific to each platform ("Likes", "Retweets", etc.).
- **Tool access & knowledge:** Our user ...
    - ... is comfortable navigating the user interfaces of Twitter and Facebook to export their own data
    - ... has a digital calendar that can export to ICS files, and is comfortable doing so
    - ... is comfortable downloading a script from GitHub to their own computer
    - ... is comfortable opening a shell and typing a few commands

## Elements of the problem statement

- **Summarize and/or aggregate individual data sources**
    - Understand formats and schemas of data exported from Facebook, Twitter, LinkedIn, Google Calendar
    - Identify meaningful summaries (e.g. total number of posts) and aggregations (e.g. total Tweets per week) for each data source
- **Synthesize across data sources to answer questions**
    - Do the user's levels of activity across different social media platforms rise and fall together, or do they cycle between one platform or another?
    - What times of day do they tend to be most active on social media?
    - How does their social media activity compare with their other activities, for example, how often does social media activity overlap with scheduled events?

## Use cases

_Each use case should provide details about the interactions between the user and the system you are building. The responses provided by the user must be consistent with the user profile. For example, you should not expect a user who is a non-programmer to do python programming. A use case should specify a series of interactions between the user and the system to accomplish one of the elements of the problem statement. You should have at least 3 use cases._

### Summarize Facebook usage

**Prerequisite:** User has downloaded data and script to the same directory, and opened a Bash terminal there

Overall number of statuses, shared statuses, links, etc. (HTML)

### Summarize Google Calendar data

(ICS)

Without a lot of analysis, we can't disaggregate different types of activities in calendar data, but we can calculate the overall number of scheduled hours in a day (with special handling for overlapping and/or all-day events)

### Identify daily temporal patterns in social media use


