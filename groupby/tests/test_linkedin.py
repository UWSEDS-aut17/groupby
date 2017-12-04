


con_df = read_safely('./connections.csv')
con_df_by_week = clean_df(con_df, 'Connected On')
invites_df = read_safely('Invitations.csv')
invites_sent, invites_received = get_sent_receive_invites(invites_df, 'Direction')
invites_sent_by_week = clean_df(invites_sent, 'Sent At')
invites_received_by_week = clean_df(invites_received, 'Sent At')
