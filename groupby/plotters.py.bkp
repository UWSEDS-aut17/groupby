import matplotlib.pyplot as plt


def plot(x,y,z, xlabel, ylabel, title, fig_size, fig_color, flag):

    try:
        fig,ax= plt.subplots(nrows=1)
        ax.bar(z[0:5],y[0:5], color = fig_color)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        if flag == '-T' or flag == '-L':
            plt.xticks(z[0:5], x[0:5])

        fig.set_size_inches(fig_size)
        return fig
    except:
        return "Can't generate plot"


def plot_tweetDate(x,y, xlabel, ylabel, title, fig_size, fig_color):
    fig,ax= plt.subplots(nrows=1)
    ax.bar(x['month'],x['tweet_id'], color = fig_color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(x['month'], y)
    fig.set_size_inches(fig_size)
    return fig

# GCAL+SOC
