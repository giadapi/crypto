import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_tweet_volume():
    df = pd.read_csv('all_columns_daily_090323.csv')

    df['negative_bert'] = df['negative_bert'] * df['daily_tweets']
    df['neutral_bert'] = df['neutral_bert'] * df['daily_tweets']
    df['positive_bert'] = df['positive_bert'] * df['daily_tweets']

    df_30 = df.iloc[-30:]

    df_30_drop = df_30.drop(['Unnamed: 0', 'neutral_bert', 'daily_tweets', 'MA7_Sentiment', 'MA20_Sentiment', 'MA50_Sentiment', 'BTC_price'], axis=1 )

    df_30_drop['negative'] = df['negative_bert']
    df_30_drop['positive'] = df['positive_bert']
    df_30_clean = df_30_drop.drop(['negative_bert','positive_bert'], axis=1 )


    #set seaborn plotting aesthetics
    sns.set(style='white')

    #create stacked bar chart
    df_30_clean.set_index('date').plot(kind='bar', stacked=True, color=['lightblue', 'orange'])

    #add overall title
    plt.title('Volume of Positive and Negative tweets', fontsize=16)

    #add axis titles
    plt.xlabel('Date')
    plt.ylabel('Volume of Tweets')

    #rotate x-axis labels
    plt.xticks(rotation=45, fontsize = 7)

if __name__ == "__main__":
    plot_tweet_volume()
