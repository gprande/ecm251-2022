import streamlit as st
from visual.home import Home
from visual.login import Login

st.set_page_config(page_title="Prandelitz Store",layout="centered",initial_sidebar_state="collapsed",menu_items=None)
if Login():
    Home()