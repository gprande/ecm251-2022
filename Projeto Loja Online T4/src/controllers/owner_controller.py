from controllers.product_controller import Product_Control
import streamlit as st
import base64

class Owner:
    def __init__(self) -> None:        
        new_product_name = st.text_input("Enter product name:",key="new_prod_name")               
        new_product_description = st.text_input("Enter game description:",key="new_prod_description")
        new_product_keyword = st.text_input("Enter product keyword:",key="new_prod_key")               
        new_product_value = st.text_input("Enter product price:",key="new_prod_value")
        new_product_image = st.file_uploader("Loads an image for the product",
                                             key="new_prod_img",
                                             accept_multiple_files=False)
        
        if st.button("Register product",key="new_prod_button"):
            if st.session_state["products"].add_new_product(new_product_name,
                                                            new_product_description,
                                                            new_product_keyword,
                                                            float(new_product_value),
                                                            new_product_image):
                st.write("Product succesfully added to database")
            else:
                st.write("We couldn't register this new product, please check if it already exists")