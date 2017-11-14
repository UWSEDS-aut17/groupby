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

- **Description:** _high level description of the roles of the component_ 
- **Inputs:** _be specific about the data types, e..g. for DataFrames, specify the column names and the types of the column values_
- **Outputs:** _same consideration as with inputs_

```
# psuedocode here
```

### read_LinkedIn_data()

- **Description:** For LinkedIn, types of connections and invites sent/received are being analyzed. This will show what period was one most active in and their interaction with LinkedIn in terms of amount of time spent in networking per week. 
- **Inputs:** Inputs consist of 2 csv files:  
1. Connections.csv - Connections.csv contain data about my LinkedIn connections. It contains the following features/columns:
<br>
a. First Name - Name
<br>
b. Last Name - Name
<br>
c. Position - Connection title/position
<br>
d. Company - Name of the company my connection works in
<br>
e. Connected_On - Date

2. Invitations.csv - Invitations.csv contain data about invitations sent and received on LinkedIn. They are being grouped by week which results in data about number of invitations sent/received per week. It contains the following features/columns.
<br>
a.From - Invitation Sender's Name
<br>
b.To - Invitation Receiver's Name
<br>
c.Sent At - Date at which Invitation was sent/received.
<br>
d.Message - Message string
<br>
e.Direction - INCOMING / OUTGOING.
  
- **Outputs:** The ouputs are dataframes obtained by reading the input csv files, with the same features/columns.  

```
# psuedocode here
```

### read_Twitter_data()

- **Description:** _high level description of the roles of the component_ 
- **Inputs:** _be specific about the data types, e..g. for DataFrames, specify the column names and the types of the column values_
- **Outputs:** _same consideration as with inputs_

```
# psuedocode here
```

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
