import matplotlib.pyplot as plt
from wordcloud import WordCloud


def plot(x,y,z, xlabel, ylabel, title, fig_size, fig_color, flag):
    plt.style.use('seaborn-white')
    try:
        fig,ax= plt.subplots(nrows=1)
        if flag == '-T':
            ax.bar(z[0:5],y[0:5], color = '#1DA1F2')

        else:
            ax.bar(z[0:5],y[0:5], color = fig_color)

        ax.set_title(title,fontsize=24,fontweight='bold')
        ax.set_xlabel(xlabel,fontsize=18)
        ax.set_ylabel(ylabel,fontsize=18)

        if flag == '-T' or flag == '-L':
            plt.xticks(z[0:5], x[0:5],fontsize=16,fontstyle='italic')
            plt.yticks(fontsize=16,fontstyle='italic')

        fig.set_size_inches(fig_size)
        return fig
    except:
        return "Can't generate plot"


def plot_tweetDate(x,y, xlabel, ylabel, title, fig_size, fig_color):
    plt.style.use('seaborn-white')
    fig,ax= plt.subplots(nrows=1)
    ax.plot(x['month'],x['tweet_id'], color = '#1DA1F2',marker='o',linewidth=2)
    ax.set_title(title,fontsize=24,fontweight='bold')
    ax.set_xlabel(xlabel,fontsize=18)
    ax.set_ylabel(ylabel,fontsize=18)
    plt.xticks(x['month'], y,fontsize=16,fontstyle='italic')
    plt.yticks(fontsize=16,fontstyle='italic')
    fig.set_size_inches(fig_size)
    return fig

def plot_wc(x):
    fig = plt.figure(figsize = (60,20))
    plt.axis("off")
    plt.title('Hashtags Word Cloud',fontsize=50,fontweight='bold' )
    wordcloud = WordCloud(background_color = 'black',width = 4000,height = 2000).generate(' '.join(str(e) for e in x))
    plt.imshow(wordcloud)
    return fig

def plot_sentiment(sentiments):
    plt.style.use('seaborn-white')
    fig,ax= plt.subplots(nrows=1)
    ax.plot(sentiments['year'],sentiments['score'], color = '#1DA1F2',marker='o',linewidth=2)
    ax.set_title('Sentiment by Year',fontsize=24,fontweight='bold')
    ax.set_xlabel('Year',fontsize=18)
    ax.set_ylabel('Average Sentiment',fontsize=18)
    plt.yticks(fontsize=16,fontstyle='italic')
    plt.xticks(sentiments['year'],fontsize=16,fontstyle='italic')
    fig.set_size_inches(16,10)
    return fig
# GCAL+SOC
