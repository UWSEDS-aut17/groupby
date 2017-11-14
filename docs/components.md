# Component design

<br>

## Component list

So that users can analyze their social media data as detailed in our use cases, we need the following components for each of our four datasets (Twitter, Facebook, LinkedIn, Google Calendar):

- **read_X_data()** - read each dataset into native data structures
- **summarize_X_data()** - calculate meaningful summary statistics and visualizations for X dataset
- **aggregate_X_data()** - aggregate selected activities for each dataset (# per day or # per week) 
- **peak_hours()** and **time_use()** - compare and analyze the aggregated versions of our datasets

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

- **Description:** _high level description of the roles of the component_ 
- **Inputs:** _be specific about the data types, e..g. for DataFrames, specify the column names and the types of the column values_
- **Outputs:** _same consideration as with inputs_

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

x4

### aggregate_X_data()

x4

### peak_hours()

- ... in aggregate
- ... broken down by platform

### time_use()
