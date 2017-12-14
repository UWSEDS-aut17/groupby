"""This script provides a brief example of using our code as a Python module.

"""

import matplotlib.pyplot as plt
import groupby.linkedin as linkedin



fname = '~/data/LinkedIn/Connections.csv'
connections_df = linkedin.open_linkedin(fname)

print(connections_df.head())

con_df_by_week = linkedin.clean_df(connections_df, 'Connected On')
connections = linkedin.plot(con_df_by_week, 'Connected On', 'count', 'Weeks', 'Number of Connections', 'Number of Connections per week', (15, 5), '#8D6CAB')
connections.savefig('connections.png')
