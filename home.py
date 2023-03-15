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
background-image: url("https://i.pinimg.com/originals/c5/cb/e4/c5cbe4d2b4d36c0f50eba2e684dda6c9.gif");
background-size: 100%;
background-position: top left;
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
st.markdown(f"<h1 style='text-align: lef; color:#FFFFFF; font-size: 80px; font-family: Oswald, sans-serif'>Let's read<br />the Voice of Twitter</h1>", unsafe_allow_html=True)

#Button
if st.button("Start now"):
    switch_page("main")
