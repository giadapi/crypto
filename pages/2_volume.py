import streamlit as st
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_extras.switch_page_button import switch_page
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from pages_functions import *

#Page overall setting
#https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="Twitter Volume Analysis | RoboStock",
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
background-image: url("https://static.wixstatic.com/media/63fd61_e5b618e5d86c4ec0b761c9b74e5e8b69~mv2.jpeg");
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

#Input data / score from other files
#Data Downloading, Processing and Visualising the Tweet Volume
vol_data = pd.read_csv('https://raw.githubusercontent.com/Endy-chow/crypto-project/mastertraining_data/complete_vol.csv',lineterminator='\n',index_col=0)
vol_data['negative_bert'] = vol_data['negative_bert'] * vol_data['daily_tweets']
vol_data['neutral_bert'] = vol_data['neutral_bert'] * vol_data['daily_tweets']
vol_data['positive_bert'] = vol_data['positive_bert'] * vol_data['daily_tweets']
vol_data_30 = vol_data.iloc[-30:]
vol_data_30_drop = vol_data_30[['date','negative_bert','neutral_bert','positive_bert']]
vol_data_30_drop['negative'] = vol_data['negative_bert']
vol_data_30_drop['positive'] = vol_data['positive_bert']
vol_data_30_clean = vol_data_30_drop.drop(['negative_bert','positive_bert'], axis=1)
#set seaborn plotting aesthetics
sns.set(style='white')
#create stacked bar chart
vol_data_30_clean.set_index('date').plot(kind='bar', stacked=True, color=['lightblue', 'orange'])
#add overall title
#plt.title('Volume of Positive and Negative tweets', fontsize=16)
#add axis titles
plt.xlabel('Date')
plt.ylabel('Volume of Tweets')

#rotate x-axis labels
plt.xticks(rotation=45, fontsize = 7)
plt.savefig('tweet_volume.png')

#Overall Score
volume_signal = "buy"
#Buy Example
volume_today_no_tweet = round(vol_today_no_tweet(vol_data))
#Sell Example


#Page Header
st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 📊 </h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; color:#FFFFFF; font-size: 40px; font-family: Open Sans, sans-serif'> Twitter Volume Analysis </h5>", unsafe_allow_html=True)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Section 1 - Twitter volume Analysis & Twitter volume Score of Today
col_1a, col_1b,  = st.columns([1,2])

#Section 1a - Twitter volume Analysis
with col_1a:

    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 10px; font-size: 50px; font-family: Open Sans Bold, sans-serif'> 📊 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 16px; font-family: Open Sans, sans-serif'> Twitter volume Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if volume_signal == "buy":
        st.markdown(f"<h5 style='text-align: center; margin-top: 0px;color:#FF914D; font-size: 30px; font-family: Oswald, sans-serif'> OPTIMISTIC </h5>", unsafe_allow_html=True)
    elif volume_signal == "hold":
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#737373; font-size: 30px; font-family: Oswald, sans-serif'> HOLD </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#4284CC; font-size: 30px; font-family: Oswald, sans-serif'> PESSIMISTIC </h5>", unsafe_allow_html=True)

#Section 1b - Twitter volume Score of Today
with col_1b:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Number of Tweets about Bitcoin Today </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {volume_today_no_tweet} </h5>", unsafe_allow_html=True)

    #Histogram
    vol_data_lastday = vol_data_30_clean.iloc[-1:]
    fig_1 = go.Figure(data=[
        go.Bar(name='negative', x=vol_data_lastday['date'], y=vol_data_lastday['negative'], marker_color='#4284CC'),
        go.Bar(name='positive', x=vol_data_lastday['date'], y=vol_data_lastday['positive'], marker_color='#FF914D')
        ])
    fig_1.update_layout(barmode='stack',legend=dict(yanchor="top",y=1,xanchor="left",x=0.01),width=382,height=200,margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig_1)

# #Section 2 (new)
with st.container():
    st.markdown(f"<h5 style='text-align: center; margin-top: 36px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Volume of Positive and Negative Tweets</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 12px; font-family: Open Sans Bold, sans-serif'> Last 30 days </h5>", unsafe_allow_html=True)
    # st.image("tweet_volume.png")
    fig = go.Figure(data=[
        go.Bar(name='negative', x=vol_data_30_clean['date'], y=vol_data_30_clean['negative'], marker_color='#4284CC'),
        go.Bar(name='positive', x=vol_data_30_clean['date'], y=vol_data_30_clean['positive'], marker_color='#FF914D')
        ])
    fig.update_layout(barmode='stack',margin=dict(l=80, r=40, t=0, b=0))
    st.plotly_chart(fig)

    #Margin
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 20px; color:#4284CC; font-size: 20px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)


# #Section 2 (old, with date input)
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

# #Section 2b - Output the Twitter volume Analysis Graph; Need to the input from Peter
# with col_2b:
#     #Column Title
#     st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Volume of Positive and Negative tweets</h5>", unsafe_allow_html=True)
#     # st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 12px; font-family: Open Sans Bold, sans-serif'> {start_date} - {end_date}</h5>", unsafe_allow_html=True)

#     #Histogram
#     st.image("tweet_volume.png")

#     # chart_period = pd.DataFrame(
#     #     np.random.randn(30, 3),
#     #     columns=["Buy", "Hold", "Sell"])
#     # st.bar_chart(vol_data_30_clean)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 40px; color:#4284CC; font-size: 20px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Button
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col4.button("Home"):
    switch_page("main")

st.markdown(f"<h5 style='text-align: center; margin-top: 30px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> 2023 © - all rights reserved by CRYPTOBOT</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 10px; font-family: Open Sans, sans-serif'> NO INVESTMENT ADVICE <br>The Content is for informational purposes only,<br> you should not construe any such information or other material as legal, tax, investment, financial, or other advice.</h5>", unsafe_allow_html=True)
