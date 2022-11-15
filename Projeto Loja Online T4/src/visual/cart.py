import streamlit as st
from datetime import datetime

class Cart:
    def __init__(self) -> None:
        col1,col2,col3 = st.columns([1.5,5,2.5],gap = "small")
        with col1:
            st.write("Remove:")
            for i in range(st.session_state["cart"].get_Product_Qty()):
                j = st.session_state["cart"].show_Products(i)
                if st.button("Remove",key = ("Remove_"+j.get_Keyword()+str(i))):
                    st.session_state["cart"].remove(j)      
        
        with col2:
            st.write("Here are your products:")
            for product in range(st.session_state["cart"].get_Product_Qty()):
                st.write(str(st.session_state["cart"].show_Products(product)))
                st.text(" ")
        
        with col3:
            st.write("Your purchase:")
            st.write("Number of products: "+str(st.session_state["cart"].get_Product_Qty()))
            st.write("Total: R$ "+str(st.session_state["cart"].get_Total()))
            if st.button("Payment",key = ("payment")):
                if st.session_state["order"].new_order(st.session_state["userlogged"],
                                                          st.session_state["cart"],
                                                          datetime.today().strftime("%d/%m/%Y")):
                    st.write("Payment page is going under maintenance to better serve you")
                else:
                    st.write("We couldn't process your order, please try again later")