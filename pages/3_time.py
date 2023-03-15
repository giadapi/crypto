import streamlit as st
import pandas as pd
import numpy as np
import datetime

from streamlit_extras.switch_page_button import switch_page

#Page overall setting
#https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="Time Series Analysis | RoboStock",
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
background-image: url("https://static.wixstatic.com/media/63fd61_ff92ed6f68af4e0ea039f75155590541~mv2.jpeg");
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
time_signal = "buy"
time_high_price = 17137.65
time_high_price_change = 0.05
time_low_price = 15237.65
time_low_price_change = -0.15


#Page Header
st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 60px; font-family: Oswald, sans-serif'> ⏳ </h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; color:#FFFFFF; font-size: 40px; font-family: Oswald, sans-serif'> Time Series Analysis </h5>", unsafe_allow_html=True)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Section 1 - Twitter Sentiment Analysis & Twitter Sentiment Score of Today
col_1a, col_1b,  col_1c = st.columns([1,1,1])

#Section 1a - Twitter Sentiment Analysis
with col_1a:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 10px; font-size: 50px; font-family: Open Sans Bold, sans-serif'> ⏳ </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Time Series Analysis </h5>", unsafe_allow_html=True)
    #Label for Buy, Hold or Sell
    if time_signal == "buy":
        st.markdown(f"<h5 style='text-align: center; margin-top: 0px;color:#FF914D; font-size: 50px; font-family: Oswald, sans-serif'> Buy </h5>", unsafe_allow_html=True)
    elif time_signal == "hold":
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#737373; font-size: 50px; font-family: Oswald, sans-serif'> HOLD </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; margin-top: 10px;color:#4284CC; font-size: 50px; font-family: Oswald, sans-serif'> SELL </h5>", unsafe_allow_html=True)


#Section 1b - Twitter Sentiment Score of Today
with col_1b:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Highest Price in coming 5 days </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 24px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {time_high_price} </h5>", unsafe_allow_html=True)
    if time_high_price_change >= 0:
        st.markdown(f"<h5 style='text-align: center; margin-top: 4px;color:#FF914D; font-size: 20px; font-family: Oswald, sans-serif'> ({time_high_price_change}) </h5>", unsafe_allow_html=True)
    elif time_high_price_change == 0:
        st.markdown(f"<h5 style='text-align: center; margin-top: 4px;color:#737373; font-size: 20px; font-family: Oswald, sans-serif'> ({time_high_price_change}) </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; margin-top: 4px;color:#4284CC; font-size: 20px; font-family: Oswald, sans-serif'> ({time_high_price_change}) </h5>", unsafe_allow_html=True)

with col_1c:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Lowest Price in coming 5 days </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 24px; color:#000000; font-size: 40px; font-family: Oswald, sans-serif'> {time_low_price} </h5>", unsafe_allow_html=True)
    if time_high_price_change >= 0:
        st.markdown(f"<h5 style='text-align: center; margin-top: 4px;color:#FF914D; font-size: 20px; font-family: Oswald, sans-serif'> ({time_low_price_change}) </h5>", unsafe_allow_html=True)
    elif time_high_price_change == 0:
        st.markdown(f"<h5 style='text-align: center; margin-top: 4px;color:#737373; font-size: 20px; font-family: Oswald, sans-serif'> ({time_low_price_change}) </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; margin-top: 4px;color:#4284CC; font-size: 20px; font-family: Oswald, sans-serif'> ({time_low_price_change}) </h5>", unsafe_allow_html=True)

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

#Section 2b - Output the Twitter Sentiment Analysis Graph; Need to the input from Peter
with col_2b:
    #Column Title
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Sentiment Histogram</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#000000; font-size: 12px; font-family: Open Sans Bold, sans-serif'> {start_date} - {end_date}</h5>", unsafe_allow_html=True)

    #Histogram
    chart_data = pd.DataFrame(
        np.random.randn(20, 2),
        columns=['a', 'b'])
    st.line_chart(chart_data)

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 40px; color:#4284CC; font-size: 20px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

#Button
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
if col4.button("Home"):
    switch_page("main")
