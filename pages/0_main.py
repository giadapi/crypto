import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card
from pages_functions import *
# from 3_time import t_signal


#Page overall setting
#https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="RoboStock",
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
with open('style_main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Background Image - Use image to control the background color
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.wixstatic.com/media/63fd61_b86a647579344fe0b43290785a1a3af0~mv2.gif");
background-size: 130%;
background-position: top right;
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



#input score from other files
vol_data = pd.read_csv('https://raw.githubusercontent.com/Endy-chow/crypto-project/mastertraining_data/complete_vol.csv',lineterminator='\n',index_col=0)
# tweet_data = pd.read_csv('~/Code/giadapi/crypto/complete_tweet_2023-03-14.csv',lineterminator='\n',index_col=0)

main_score = sent_score(vol_data)
sentiment_signal = sent_rating(main_score)
volume_signal = vol_string_return(vol_data)
time_signal = "sell"

with st.container():
#Section 1a - Key Message
    #margin
    st.markdown(f"<h5 style='text-align: center; margin-top: 30px;color:#4284CC; font-size: 10px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 26px; font-family: Oswald, sans-serif'> Twitter says ... </h5>", unsafe_allow_html=True)
    #Section 1b - Buy or Sell
    if main_score >= 0.6:
        st.markdown(f"<h5 style='text-align: center; color:#FF914D; font-size: 50px; font-family: Oswald, sans-serif'> OPTIMISTIC TODAY 🐂 </h5>", unsafe_allow_html=True)
    elif main_score >= 0.4:
        st.markdown(f"<h5 style='text-align: center; color:#FF914D; font-size: 50px; font-family: Oswald, sans-serif'> HOLD TODAY 🐂 </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 50px; font-family: Oswald, sans-serif'> PESSIMISTIC TODAY 🧸 </h5>", unsafe_allow_html=True)

    #Section 1c - Score bar
    col_a1, col_a2, col_a3 = st.columns([1,4,1])
    with col_a1:
        st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 🧸 </h5>", unsafe_allow_html=True)
    with col_a2:
        st.progress(main_score, text=None)
    with col_a3:
        st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 🐂 </h5>", unsafe_allow_html=True)

    #margin
    st.markdown(f"<h5 style='text-align: center; margin-top: 30px;color:#4284CC; font-size: 10px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

col_b1, col_b2 = st.columns([1,1])
with col_b1:
    #Column Title
    st.image("https://static.wixstatic.com/media/63fd61_6dfc87ea0cd94e539e91a960df3c8366~mv2.png")
    # st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> 💬 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#FF914D; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Sentiment Analysis </h5>", unsafe_allow_html=True)

    # #Label for Buy, Hold or Sell
    # if sentiment_signal == "buy":
    #     st.image("https://static.wixstatic.com/media/63fd61_9c62560397124eaa8c320e49d4b76408~mv2.png")
    # elif sentiment_signal == "hold":
    #     st.image("https://static.wixstatic.com/media/63fd61_f32341a3d588440fb1bd2b2ff692e29e~mv2.png")
    # else:
    #     st.image("https://static.wixstatic.com/media/63fd61_2f1ddec84fd2427f86035f8ad0d54325~mv2.png")


    if st.button("Read More"):
        switch_page("sentiment")

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

with col_b2:
    #Column Title
    st.image("https://static.wixstatic.com/media/63fd61_a525a4f28cd74e418f5448ef0403f0ba~mv2.png")
    #st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> 📊 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Volume Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    # if volume_signal == "high":
    #     st.image("https://static.wixstatic.com/media/63fd61_9c62560397124eaa8c320e49d4b76408~mv2.png")
    # # elif volume_signal == "hold":
    # #     st.image("https://static.wixstatic.com/media/63fd61_f32341a3d588440fb1bd2b2ff692e29e~mv2.png")
    # else:
    #     st.image("https://static.wixstatic.com/media/63fd61_2f1ddec84fd2427f86035f8ad0d54325~mv2.png")

    if st.button("Read more "):
        switch_page("volume")

    #Margin
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

# with col_b3:
#     #Column Title
#     st.image("https://static.wixstatic.com/media/63fd61_a7725d3f2adf4c8b9e6401e344422823~mv2.png")
#     #st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> ⏳ </h5>", unsafe_allow_html=True)
#     st.markdown(f"<h5 style='text-align: left; color:#151515; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Time Series Analysis </h5>", unsafe_allow_html=True)

#     #Label for Buy, Hold or Sell
#     if time_signal == "buy":
#         st.image("https://static.wixstatic.com/media/63fd61_9c62560397124eaa8c320e49d4b76408~mv2.png")
#     elif time_signal == "hold":
#         st.image("https://static.wixstatic.com/media/63fd61_f32341a3d588440fb1bd2b2ff692e29e~mv2.png")
#     else:
#         st.image("https://static.wixstatic.com/media/63fd61_2f1ddec84fd2427f86035f8ad0d54325~mv2.png")

#     if st.button("Read More  "):
#         switch_page("time")

#     #Margin
#     st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#FFFFFF; font-size: 10px; font-family: Open Sans, sans-serif'> 2023 © - all rights reserved by CRYPTOBOT</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#FFFFFF; font-size: 10px; font-family: Open Sans, sans-serif'> NO INVESTMENT ADVICE <br>The Content is for informational purposes only,<br> you should not construe any such information or other material as legal, tax, investment, financial, or other advice.</h5>", unsafe_allow_html=True)
