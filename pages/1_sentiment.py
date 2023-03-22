import streamlit as st
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib
from streamlit_extras.switch_page_button import switch_page
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from pages_functions import *

from streamlit_extras.switch_page_button import switch_page

#Page overall setting
#https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="Twitter Sentiment Analysis | RoboStock",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

#Disble the sidebar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

#Import the CSS file for website design format
with open('style_page.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Background Image - Use image to control the background color
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.wixstatic.com/media/63fd61_b1ee9b9181f047fe873c298385a8269f~mv2.jpeg");
background-size: 110%;
background-position: top;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

vol_data = pd.read_csv('https://raw.githubusercontent.com/Endy-chow/crypto-project/master/training_data/complete_vol.csv',lineterminator='\n',index_col=0)
tweet_data = pd.read_csv('https://raw.githubusercontent.com/Endy-chow/crypto-project/master/training_data/complete_tweet.csv',lineterminator='\n',index_col=0)

sentiment_score = round(sent_score(vol_data),3)
sentiment_buy_example_1,sentiment_buy_example_2,sentiment_buy_example_3,sentiment_buy_example_score_1,sentiment_buy_example_score_2,sentiment_buy_example_score_3 = sentiment_buy(tweet_data,start_date=None,end_date=None)

sentiment_signal = sent_rating(sentiment_score)
sentiment_sell_example_1, sentiment_sell_example_2, sentiment_sell_example_3, sentiment_sell_example_score_1, sentiment_sell_example_score_2, sentiment_sell_example_score_3 = sentiment_sell(tweet_data,start_date=None,end_date=None)



# #Input score from other files
# data = pd.read_csv('~/code/giadapi/crypto/data/all_columns_daily_090323.csv')
# #Overall Score
# sentiment_signal = "buy"
# sentiment_score = 0.678
# #Buy Example
# sentiment_buy_example_1 = "Bitcoin to hedge against the results of years of Congressonal, Treasury and Federal Reserve policy."
# sentiment_buy_example_score_1 = 0.776
# sentiment_buy_example_2 = "When you dig deeper into #kardiachain company and its partners (Transportation, Real Estate, Electronics and #Crypto projects), you know that you better have to load heavy bags of $KAI. Buy your moon tickets now or regret it forever. #Bitcoin #ethereum #blockchain $btc $eth $dot"
# sentiment_buy_example_score_2 = 0.690
# sentiment_buy_example_3 = "Take that stimulus fiat and put it into Can get 8.6% on your dollars.  Get interest on your #Bitcoin too."
# sentiment_buy_example_score_3 = 0.595
# #Sell Example
# sentiment_sell_example_1 = " Oh no... #bitcoin isn’t piramidal #bitcoin is a red the valor."
# sentiment_sell_example_score_1 = 0.134
# sentiment_sell_example_2 = " #Bitcoin doesn’t need Satoshi Nakamoto"
# sentiment_sell_example_score_2 = 0.256
# sentiment_sell_example_3 = "Bitcoin blocks delay in last day #BTC #bitcoin #R #ggplot2"
# sentiment_sell_example_score_3 = 0.278


#Page Header
st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 60px; font-family: Oswald, sans-serif'> 💬 </h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; color:#FFFFFF; font-size: 40px; font-family: Open Sans, sans-serif'> Twitter Sentiment Analysis </h5>", unsafe_allow_html=True)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Section 1 - Twitter Sentiment Analysis & Twitter Sentiment Score of Today
col_1a, col_1b,  = st.columns([1,2])

#Section 1a - Twitter Sentiment Analysis
with col_1a:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 10px; font-size: 50px; font-family: Open Sans Bold, sans-serif'> 💬 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color:#FF914D; font-size: 16px; font-family: Open Sans, sans-serif'> Twitter Sentiment Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if sentiment_signal == "buy":
        st.markdown(f"<h5 style='text-align: center; margin-top: 0px;color:#FF914D; font-size: 30px; font-family: Oswald, sans-serif'> OPTIMISTIC </h5>", unsafe_allow_html=True)
    elif sentiment_signal == "hold":
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#737373; font-size: 30px; font-family: Oswald, sans-serif'> HOLD </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#4284CC; font-size: 30px; font-family: Oswald, sans-serif'> PESSIMISTIC </h5>", unsafe_allow_html=True)

#Section 1b - Twitter Sentiment Score of Today
with col_1b:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Score of Today</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 6px; color:#000000; font-size: 60px; font-family: Oswald, sans-serif'> {sentiment_score} </h5>", unsafe_allow_html=True)
    #Label for Buy, Hold or Sell
    if sentiment_signal == "buy":
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px; font-size: 50px; font-family: Oswald, sans-serif'> 🥰 </h5>", unsafe_allow_html=True)
    elif sentiment_signal == "hold":
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px; font-size: 50px; font-family: Oswald, sans-serif'> 😐 </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; font-size: 50px; font-family: Oswald, sans-serif'> 😥 </h5>", unsafe_allow_html=True)

data2 = vol_data.iloc[-30:]
data2['neg_adj']=data2['negative_bert']/ (data2['negative_bert'] + data2['positive_bert'])
data2['pos_adj']=data2['positive_bert']/ (data2['negative_bert'] + data2['positive_bert'])
fig, ax3 = plt.subplots(figsize=(10,2))
# ax3.set_axis_off()
ax3.xaxis.set_major_locator(md.DayLocator(interval=5))
ax3.set_yticklabels(['{:,.0%}'.format(x) for x in ax3.get_yticks()])
ax3.stackplot(data2.date, data2.neg_adj, data2.pos_adj)
# fig2 = matplotlib.ax3.Axes.get_figure()

#Section 2 - New Graph
with st.container():
    st.markdown(f"<h5 style='text-align: center; margin-top: 36px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Histogram of Twitter Sentiment Analysis  </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 12px; font-family: Open Sans, sans-serif'> Last 30 days </h5>", unsafe_allow_html=True)
    st.pyplot(fig)

    #Margin
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 20px; color:#4284CC; font-size: 20px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

# #Section 2(Old)
# col_2a, col_2b,  = st.columns([1,2])
# #Section 2a - Input the Start and End Date
# with col_2a:
#     #Start Data
#     st.markdown(f"<h5 style='text-align: left; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Date Range </h5>", unsafe_allow_html=True)
#     start_date = st.date_input(
#         "Start Date",
#         datetime.date(2023, 2, 14))
#     end_date = st.date_input(
#         "End Date",
#         datetime.date(2023, 3, 14))

# #Section 2b - Output the Twitter Sentiment Analysis Graph; Need to the input from Peter
# with col_2b:
#     #Column Title
#     st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Histogram of Twitter Sentiment Analysis </h5>", unsafe_allow_html=True)
#     st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 12px; font-family: Open Sans Bold, sans-serif'> {start_date} - {end_date}</h5>", unsafe_allow_html=True)

#     #Histogram
#     chart_data = pd.DataFrame(
#         np.random.randn(20, 2),
#         columns=['a', 'b'])
#     st.line_chart(chart_data)

#Section 3 - Tweet's example - For Buy

#Header
st.markdown(f"<h5 style='text-align: center; margin-top: 20px; margin-bottom: 10px; color:#000000; font-size: 24px; font-family: Open Sans Bold, sans-serif'> 🐂 Tweet Samples - For Buy Signal 🔼 </h5>", unsafe_allow_html=True)

col_3a, col_3b, col_3c = st.columns([1,1,1])
with col_3a:
    #Score
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> Sentiment Score</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {sentiment_buy_example_score_1} </h5>", unsafe_allow_html=True)
    #Tweet Example
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#FF914D; font-size: 12px; font-family: Open Sans, sans-serif'> {sentiment_buy_example_1}</h5>", unsafe_allow_html=True)

with col_3b:
     #Score
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> Sentiment Score</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {sentiment_buy_example_score_2} </h5>", unsafe_allow_html=True)
    #Tweet Example
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#FF914D; font-size: 12px; font-family: Open Sans, sans-serif'> {sentiment_buy_example_2}</h5>", unsafe_allow_html=True)

with col_3c:
    #Score
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> Sentiment Score</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {sentiment_buy_example_score_3} </h5>", unsafe_allow_html=True)
    #Tweet Example
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#FF914D; font-size: 12px; font-family: Open Sans, sans-serif'> {sentiment_buy_example_3}</h5>", unsafe_allow_html=True)

#Section 4 - Tweet's example - For Sell
#Header
st.markdown(f"<h5 style='text-align: center; margin-top: 20px; margin-bottom: 10px; color:#000000; font-size: 24px; font-family: Open Sans Bold, sans-serif'> 🧸 Tweet Samples - For Sell Signal 🔽 </h5>", unsafe_allow_html=True)
col_4a, col_4b, col_4c = st.columns([1,1,1])
with col_4a:
    #Score
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> Sentiment Score</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {sentiment_sell_example_score_1} </h5>", unsafe_allow_html=True)
    #Tweet Example
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#4284CC; font-size: 12px; font-family: Open Sans, sans-serif'> {sentiment_sell_example_1}</h5>", unsafe_allow_html=True)

with col_4b:
     #Score
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> Sentiment Score</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {sentiment_sell_example_score_2} </h5>", unsafe_allow_html=True)
    #Tweet Example
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#4284CC; font-size: 12px; font-family: Open Sans, sans-serif'> {sentiment_sell_example_2}</h5>", unsafe_allow_html=True)

with col_4c:
    #Score
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> Sentiment Score</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {sentiment_sell_example_score_3} </h5>", unsafe_allow_html=True)
    #Tweet Example
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#4284CC; font-size: 12px; font-family: Open Sans, sans-serif'> {sentiment_sell_example_3}</h5>", unsafe_allow_html=True)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 40px; color:#4284CC; font-size: 20px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Button
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col4.button("Home"):
    switch_page("main")

st.markdown(f"<h5 style='text-align: center; margin-top: 30px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> 2023 © - all rights reserved by CRYPTOBOT</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> NO INVESTMENT ADVICE <br>The Content is for informational purposes only,<br> you should not construe any such information or other material as legal, tax, investment, financial, or other advice.</h5>", unsafe_allow_html=True)
