import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib
import seaborn as sns
import datetime
from datetime import timedelta

def sent_score(vol_data):
    pos = vol_data.columns.get_loc("positive_bert")
    sentiment_signal = vol_data.iloc[-1,pos]
    return sentiment_signal

def vol_signal(vol_data):
    vol = vol_data.columns.get_loc("daily_tweets")
    volume_signal = vol_data.iloc[-1,vol]
    return volume_signal

def vol_string_return(vol_data):
    vol = vol_data.columns.get_loc("daily_tweets")
    y = vol_data.iloc[-30:,vol].mean()
    v_signal = vol_signal(vol_data)
    if v_signal >= y:
        return "high"
    else:
        return "low"



def sentiment_buy(tweet_data,start_date=None,end_date=None):
    pos = tweet_data.columns.get_loc("positive_bert")
    tweet = tweet_data.columns.get_loc("text")
    d = tweet_data.columns.get_loc("date")
    if start_date == None:
        start_date = datetime.date.today()
        start_date = start_date.strftime("%Y-%m-%d")
        if start_date != tweet_data.iloc[-1,d]:
            start_date = tweet_data.iloc[-1,d]
    start_date_index = tweet_data.index[tweet_data['date']==start_date].min()
    if end_date == None:
        temp = tweet_data.iloc[start_date_index:,:]
        max_1 = temp['positive_bert'].idxmax()
        temp.drop(max_1,inplace=True)
        max_2 = temp['positive_bert'].idxmax()
        temp.drop(max_2,inplace=True)
        max_3 = temp['positive_bert'].idxmax()
        temp.drop(max_3,inplace=True)
        sentiment_buy_example_1 = tweet_data.iloc[max_1,tweet]
        sentiment_buy_example_2 = tweet_data.iloc[max_2,tweet]
        sentiment_buy_example_3 = tweet_data.iloc[max_3,tweet]
        sentiment_buy_score_1 = round(tweet_data.iloc[max_1,pos],3)
        sentiment_buy_score_2 = round(tweet_data.iloc[max_2,pos],3)
        sentiment_buy_score_3 = round(tweet_data.iloc[max_3,pos],3)
        return sentiment_buy_example_1,sentiment_buy_example_2,sentiment_buy_example_3,sentiment_buy_score_1,sentiment_buy_score_2,sentiment_buy_score_3
    else:
        end_date_index = tweet_data.index[tweet_data['date']==end_date].max()
        temp = tweet_data.iloc[start_date_index:end_date_index+1,:]
        max_1 = temp['positive_bert'].idxmax()
        temp.drop(max_1,inplace=True)
        max_2 = temp['positive_bert'].idxmax()
        temp.drop(max_2,inplace=True)
        max_3 = temp['positive_bert'].idxmax()
        temp.drop(max_3,inplace=True)
        sentiment_buy_example_1 = tweet_data.iloc[max_1,tweet]
        sentiment_buy_example_2 = tweet_data.iloc[max_2,tweet]
        sentiment_buy_example_3 = tweet_data.iloc[max_3,tweet]
        sentiment_buy_score_1 = round(tweet_data.iloc[max_1,pos],3)
        sentiment_buy_score_2 = round(tweet_data.iloc[max_2,pos],3)
        sentiment_buy_score_3 = round(tweet_data.iloc[max_3,pos],3)
        return sentiment_buy_example_1,sentiment_buy_example_2,sentiment_buy_example_3,sentiment_buy_score_1,sentiment_buy_score_2,sentiment_buy_score_3

def sentiment_sell(tweet_data,start_date=None,end_date=None):
    pos = tweet_data.columns.get_loc("negative_bert")
    tweet = tweet_data.columns.get_loc("text")
    d = tweet_data.columns.get_loc("date")
    if start_date == None:
        start_date = datetime.date.today()
        start_date = start_date.strftime("%Y-%m-%d")
        if start_date != tweet_data.iloc[-1,d]:
            start_date = tweet_data.iloc[-1,d]
    start_date_index = tweet_data.index[tweet_data['date']==start_date].min()
    if end_date == None:
        temp = tweet_data.iloc[start_date_index:,:]
        max_1 = temp['negative_bert'].idxmax()
        temp.drop(max_1,inplace=True)
        max_2 = temp['negative_bert'].idxmax()
        temp.drop(max_2,inplace=True)
        max_3 = temp['negative_bert'].idxmax()
        temp.drop(max_3,inplace=True)
        sentiment_buy_example_1 = tweet_data.iloc[max_1,tweet]
        sentiment_buy_example_2 = tweet_data.iloc[max_2,tweet]
        sentiment_buy_example_3 = tweet_data.iloc[max_3,tweet]
        sentiment_buy_score_1 = round(tweet_data.iloc[max_1,pos],3)
        sentiment_buy_score_2 = round(tweet_data.iloc[max_2,pos],3)
        sentiment_buy_score_3 = round(tweet_data.iloc[max_3,pos],3)
        return sentiment_buy_example_1,sentiment_buy_example_2,sentiment_buy_example_3,sentiment_buy_score_1,sentiment_buy_score_2,sentiment_buy_score_3
    else:
        end_date_index = tweet_data.index[tweet_data['date']==end_date].max()
        temp = tweet_data.iloc[start_date_index:end_date_index+1,:]
        max_1 = temp['negative_bert'].idxmax()
        temp.drop(max_1,inplace=True)
        max_2 = temp['negative_bert'].idxmax()
        temp.drop(max_2,inplace=True)
        max_3 = temp['negative_bert'].idxmax()
        temp.drop(max_3,inplace=True)
        sentiment_buy_example_1 = tweet_data.iloc[max_1,tweet]
        sentiment_buy_example_2 = tweet_data.iloc[max_2,tweet]
        sentiment_buy_example_3 = tweet_data.iloc[max_3,tweet]
        sentiment_buy_score_1 = round(tweet_data.iloc[max_1,pos],3)
        sentiment_buy_score_2 = round(tweet_data.iloc[max_2,pos],3)
        sentiment_buy_score_3 = round(tweet_data.iloc[max_3,pos],3)
        return sentiment_buy_example_1,sentiment_buy_example_2,sentiment_buy_example_3,sentiment_buy_score_1,sentiment_buy_score_2,sentiment_buy_score_3

def vol_today_no_tweet(vol_data):
    daily_tweets = vol_data.columns.get_loc("daily_tweets")
    volume_today_no_tweet = vol_data.iloc[-1,daily_tweets]
    return volume_today_no_tweet

def sent_rating(sent_score):
    if sent_score>=0.6:
        return "buy"
    elif sent_score>0.4:
        return "hold"
    else:
        return "sell"


# def historical_graph(vol_data):
#     matplotlib.rc_file_defaults()

#     elon_add_BTC = vol_data['date'][26]
#     elon_add_BTC_anno = vol_data['date'][31]
#     elon_add_BTC_text = '''Elon Musk adds #bitcoin
#     to his twitter profile amind
#     rumours of Tesla accepting
#     Bitcoin payments'''
#     elon_lose_BTC = vol_data['date'][131]
#     elon_lose_BTC_anno = vol_data['date'][136]
#     elon_lose_BTC_text = '''Tesla stops accepting Bitcoin
#     as payment for its cars due to
#     concerns about its carbon emissions'''

#     ax1 = sns.set_style("whitegrid")

#     fig, ax1 = plt.subplots(figsize=(40,8))

#     sns.lineplot(x = vol_data['date'], y=vol_data['BTC_price'], sort = False, color='blue',legend='brief')

#     ax2 = ax1.twinx()
#     sns.lineplot(x = vol_data['date'], y=vol_data['MA7_Sentiment'], sort = False, ax=ax2, color='orange',legend='brief').set_xticklabels
#     ax2.xaxis.set_major_locator(md.MonthLocator())
#     ax2.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
#     ax2.axvline(elon_add_BTC, color = 'red')
#     ax2.axvline(elon_lose_BTC, color = 'red')

#     ax1.legend(vol_data[['BTC_price','MA7_Sentiment']], loc='upper right')

#     plt.text(x=elon_add_BTC_anno, y=0.34,s=elon_add_BTC_text, horizontalalignment='left', size='medium', color='black', weight='semibold', backgroundcolor = 'white')
#     plt.text(x=elon_lose_BTC_anno, y=0.34,s=elon_lose_BTC_text, horizontalalignment='left', size='medium', color='black', weight='semibold', backgroundcolor = 'white')

#     plt.grid()
#     return fig
