import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#Page overall setting
#https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="RoboStock",
    page_icon="📈",
    layout="wide",
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


#Background image
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.wixstatic.com/media/63fd61_b86a647579344fe0b43290785a1a3af0~mv2.gif");
background-size: 115%;
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

#Title
st.markdown(f"<h1 style='text-align: lef; color:#FF914D; font-size: 80px; font-family: Oswald, sans-serif'>BUY or SELL <br /> Bitcoins?</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: lef; margin-bottom: 40px; color:#FFFFFF; font-size: 40px; font-family: Open Sans, sans-serif'>Let's Hear the Voice of Twitter</h1>", unsafe_allow_html=True)

col_1, col_2 = st.columns([12,2])
with col_1:
    #Button
    if st.button("Start now"):
        switch_page("main")
    st.markdown(f"<h5 style='text-align: left; margin-top: 60px; color:#FFFFFF; font-size: 10px; font-family: Open Sans, sans-serif'> 2023 © - all rights reserved by CRYPTOBOT</h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; margin-top: 0px; color:#FFFFFF; font-size: 10px; font-family: Open Sans, sans-serif'> NOT FINANCIAL ADVICE <br>The Content is for informational purposes only,<br> you should not construe any such information or other material as legal, tax, investment, financial, or other advice.</h5>", unsafe_allow_html=True)
with col_2:
    st.image("https://static.wixstatic.com/media/63fd61_4cda0de329e04f15b1e26766d4d8a946~mv2.png")
