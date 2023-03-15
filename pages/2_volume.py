import streamlit as st
import pandas as pd
import numpy as np
import datetime

from streamlit_extras.switch_page_button import switch_page

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
with open('style_main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Background Image - Use image to control the background color
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.wixstatic.com/media/63fd61_e5b618e5d86c4ec0b761c9b74e5e8b69~mv2.jpeg");
background-size: 1600px;
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

#Input score from other files
#Overall Score
volume_signal = "buy"
#Buy Example
volume_today_no_tweet = 1100000000
#Sell Example
volume_sell_example_1 = " Oh no... #bitcoin isn’t piramidal #bitcoin is a red the valor."
volume_sell_example_score_1 = 0.134
volume_sell_example_2 = " #Bitcoin doesn’t need Satoshi Nakamoto"
volume_sell_example_score_2 = 0.256
volume_sell_example_3 = "Bitcoin blocks delay in last day #BTC #bitcoin #R #ggplot2"
volume_sell_example_score_3 = 0.278


#Page Header
st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 📊 </h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; color:#FFFFFF; font-size: 40px; font-family: Oswald, sans-serif'> Twitter Volume Analysis </h5>", unsafe_allow_html=True)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Section 1 - Twitter volume Analysis & Twitter volume Score of Today
col_1a, col_1b,  = st.columns([1,2])

#Section 1a - Twitter volume Analysis
with col_1a:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 10px; font-size: 50px; font-family: Open Sans Bold, sans-serif'> 📊 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter volume Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if volume_signal == "buy":
        st.markdown(f"<h5 style='text-align: center; margin-top: 0px;color:#FF914D; font-size: 50px; font-family: Oswald, sans-serif'> Buy </h5>", unsafe_allow_html=True)
    elif volume_signal == "hold":
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#737373; font-size: 50px; font-family: Oswald, sans-serif'> HOLD </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#4284CC; font-size: 50px; font-family: Oswald, sans-serif'> SELL </h5>", unsafe_allow_html=True)


#Section 1b - Twitter volume Score of Today
with col_1b:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Number of Tweet about Bitcoin Today </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 6px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {volume_today_no_tweet} </h5>", unsafe_allow_html=True)

    #Histogram
    chart_today = pd.DataFrame(
        np.random.randn(1, 3),
        columns=["Buy", "Hold", "Sell"])
    st.bar_chart(chart_today)

#Section 2
col_2a, col_2b,  = st.columns([1,2])
#Section 2a - Input the Start and End Date
with col_2a:
    #Start Data
    st.markdown(f"<h5 style='text-align: left; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Date Range </h5>", unsafe_allow_html=True)
    start_date = st.date_input(
        "Start Date",
        datetime.date(2023, 2, 14))
    end_date = st.date_input(
        "End Date",
        datetime.date(2023, 3, 14))

#Section 2b - Output the Twitter volume Analysis Graph; Need to the input from Peter
with col_2b:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Volume Analysis</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 12px; font-family: Open Sans Bold, sans-serif'> {start_date} - {end_date}</h5>", unsafe_allow_html=True)

    #Histogram
    chart_period = pd.DataFrame(
        np.random.randn(30, 3),
        columns=["Buy", "Hold", "Sell"])
    st.bar_chart(chart_period)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 40px; color:#4284CC; font-size: 20px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Button
if st.button("Home Page"):
    switch_page("main")
