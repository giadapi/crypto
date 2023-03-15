import streamlit as st
import numpy as np

from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card

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
# page_bg_img = f"""
# <style>
# [data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://i.pinimg.com/originals/c5/cb/e4/c5cbe4d2b4d36c0f50eba2e684dda6c9.gif");
# background-size: 100%;
# background-position: top left;
# background-repeat: no-repeat;
# background-attachment: local;
# }}
# [data-testid="stHeader"] {{
# background: rgba(0,0,0,0);
# }}
# [data-testid="stToolbar"] {{
# right: 2rem;
# }}
# </style>
# """
# st.markdown(page_bg_img, unsafe_allow_html=True)

"""
For Data Downloading and Create Graphic
"""



#input score from other files
main_score = 0.8
sentiment_signal = "buy"
volume_signal = "buy"
time_signal = "buy"

#Section 1a - Key Message
st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 26px; font-family: Oswald, sans-serif'> Twitter says ... </h5>", unsafe_allow_html=True)

#Section 1b - Buy or Sell
if main_score >= 0.6:
    st.markdown(f"<h5 style='text-align: center; color:#FF914D; font-size: 80px; font-family: Oswald, sans-serif'> BUY TODAY 🐂 </h5>", unsafe_allow_html=True)
elif main_score >= 0.4:
    st.markdown(f"<h5 style='text-align: center; color:#FF914D; font-size: 80px; font-family: Oswald, sans-serif'> HOLD TODAY 🐂 </h5>", unsafe_allow_html=True)
else:
    st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 80px; font-family: Oswald, sans-serif'> SELL TODAY 🧸 </h5>", unsafe_allow_html=True)

#Section 1c - Score bar
col_a1, col_a2, col_a3 = st.columns([1,4,1])
with col_a1:
    st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 🧸 </h5>", unsafe_allow_html=True)
with col_a2:
    st.progress(main_score, text=None)
with col_a3:
    st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 🐂 </h5>", unsafe_allow_html=True)


st.markdown(f"<h5 style='text-align: center; margin-top: 30px;color:#4284CC; font-size: 10px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)


# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)

# for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1, text=progress_text)

# with st.container():
#    st.bar_chart(np.random.randn(50, 3))

# col_a1, col_a2 = st.columns([2,1])
# col_a1.metric("Temperature", "70 °F", "1.2 °F")
# col_a2.metric("Wind", "9 mph", "-8%")

# st.markdown(f"<h1 style='text-align: center; color:#FF914D;'>Some title</h1>", unsafe_allow_html=True)

col_b1, col_b2, col_b3 = st.columns([1,1,1])
with col_b1:
    #Column Title
    st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> 💬 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#FF914D; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Sentiment Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if sentiment_signal == "buy":
        st.markdown(f"BUY")
    elif sentiment_signal == "hold":
        st.markdown(f"HOLD")
    else:
        st.markdown(f"SELL")

    if st.button("Analysis Now 1"):
        switch_page("sentiment_suraj")

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

with col_b2:
    #Column Title
    st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> 📊 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Volume Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if volume_signal == "buy":
        st.markdown(f"BUY")
    elif volume_signal == "hold":
        st.markdown(f"HOLD")
    else:
        st.markdown(f"SELL")

    if st.button("Analysis Now 2"):
        switch_page("volume")

    #Margin
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

with col_b3:
    #Column Title
    st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> ⏳ </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#951ABE; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Time Series Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if time_signal == "buy":
        st.markdown(f"BUY")
    elif time_signal == "hold":
        st.markdown(f"HOLD")
    else:
        st.markdown(f"SELL")

    if st.button("Analysis Now 3"):
        switch_page("time")

    #Margin
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

# col_b4.metric("Temperature", "70 °F", "1.2 °F")

#below blocks are testing purpose only
# col_a1, col_a2 = st.columns([2,1])
# col_a1.metric("Temperature", "70 °F", "1.2 °F")
# col_a2.metric("Wind", "9 mph", "-8%")

# with col_b1:
#     card(
#         title="Hello World! 1",
#         text="Some description",
#         image="http://placekitten.com/300/250",
#         url="http://localhost:8501/sentiment",
#     )

# with col_b2:
#     card(
#         title="Hello World! 2",
#         text="Some description",
#         image="http://placekitten.com/300/250",
#         url="http://localhost:8501/sentiment",
#     )
