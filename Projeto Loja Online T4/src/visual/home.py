import streamlit as st
from controllers.product_controller import Product_Control
from controllers.cart_controller import Cart_Control
from controllers.order_controller import Order_Control
from controllers.owner_controller import Owner
from visual.cart import Cart
from visual.profile import Profile
from visual.info import Info

class Home:
    def __init__(self):
        if "cart" not in st.session_state:
            st.session_state["cart"] = Cart_Control()
        st.session_state["products"] = Product_Control()
        st.session_state["order"] = Order_Control()
        
        store,cart,profile,adm = st.tabs(["Store","Cart","Profile","Products (Admins Only)"])    
        with store:
            Info()
        with cart:
            Cart()
        with profile:
            Profile()
        with adm:
            Owner()
        
        hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
        st.markdown(hide_menu_style, unsafe_allow_html=True)