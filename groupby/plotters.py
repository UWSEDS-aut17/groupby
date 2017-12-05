
"""

# TWITTER


def plot(x,y,z, xlabel, ylabel, title, fig_size, fig_color):
    fig,ax= plt.subplots(nrows=1)
    ax.bar(z[0:5],y[0:5], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(z[0:5], x[0:5])
    fig.set_size_inches(fig_size)
    return


def plot_tweetDate(x,y, xlabel, ylabel, title, fig_size, fig_color):
    fig,ax= plt.subplots(nrows=1)
    ax.bar(x['month'],x['tweet_id'], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(x['month'], y)
    fig.set_size_inches(fig_size)
    return


# FACEBOOK

def plot(df, x,y, xlabel, ylabel, title, fig_size, fig_color):
    """
    Standard helper plot function
    """
    fig,ax= plt.subplots(nrows=1)
    ax.bar(df[x],df[y], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
#    plt.xticks(df[x], label)
    fig.set_size_inches(fig_size)
    return

# LINKEDIN

def plot(df, x,y, xlabel, ylabel, title, fig_size, fig_color):
    fig,ax= plt.subplots(nrows=1)
    ax.bar(df[x],df[y], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.set_size_inches(fig_size)
    return

# GCAL+SOC

"""
