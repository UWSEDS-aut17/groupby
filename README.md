
# ANALYSIS OF SOCIAL MEDIA DATA

## Project Description

![](doc/project-vision.png)

Browsing, interacting, and creating content on social media has become a way of life for many people. Although one's [personal Facebook data](https://www.facebook.com/help/131112897028467), [Twitter data](https://support.twitter.com/articles/20170160#), and other social media data can be downloaded, there appears to be a dearth of tools to facilitate analysis of that data--for example, [NameGenWeb](https://github.com/oxfordinternetinstitute/NameGenWeb) was created by the Oxford Internet Institute to assist Facebook users in exporting their networks, but the tool is no longer maintained or usable. 

Because we believe that social media users--not only marketers--deserve to understand their social media behavior, we are attempting a tool project that will enable users to gain very simple insights into their social media use. In addition to providing some summary of activities on each platform, we anticipate enabling users to explore several questions that depend on integration of data sources:

- Do their levels of activity across different social media platforms rise and fall together, or do they cycle between one platform or another? 
- What times of day do they tend to be most active on social media?
- How does their social media activity compare with their other activities, for example, how often does social media activity overlap with scheduled events?


## Getting Started

### Obtain your data

#### Export your social media data

To use this tool, you must download and unzip ***at least one*** of these datasets from a personal social media account (note that there can be a delay of a day or so, depending on the platform):

- Facebook - [Official instructions](https://www.facebook.com/help/131112897028467)
- Twitter - [Official instructions](https://support.twitter.com/articles/20170160#)
- LinkedIn - [Official instructions](https://www.linkedin.com/help/linkedin/answer/50191/accessing-your-account-data?lang=en)

#### Download your calendar data

Calendar data can be analyzed ***in addition*** to one or more social media datasets:

- Google Calendar - [Official instructions](https://support.google.com/calendar/answer/37111?hl=en)

### Install this tool

#### Instructions

- Clone the github repo: [https://github.com/UWSEDS-aut17/groupby.git](https://github.com/UWSEDS-aut17/groupby.git)
- From the command line, navigate to the repo and run these commands:
  - `python setup.py install`
  - `pip install -r requirements.txt`

#### Requirements

- pandas
- collections
- datetime
- icalendar
- pytz
- numpy
- seaborn
- matplotlib.pyplot


