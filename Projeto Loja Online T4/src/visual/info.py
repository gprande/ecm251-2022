import streamlit as st

class Info:
    def __init__(self) -> None:
        st.subheader("Check it out!")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        c10,c11,c12 = st.columns(3,gap="small")
        column = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12]
        
        if "var_columns" not in st.session_state:
            st.session_state["var_columns"] = 0
            
        product_qty = st.session_state["products"].get_Product_Qty()
        for st.session_state["var_columns"] in range(product_qty):
            with column[st.session_state["var_columns"]]:
                st.image(st.session_state["products"].get_Product(st.session_state["var_columns"]).get_Image(), st.session_state["products"].get_Product(st.session_state["var_columns"]).get_Description())
                st.write("R$ "+ str(st.session_state["products"].get_Product(st.session_state["var_columns"]).get_Value()))
                if st.button("Add to cart", key = st.session_state["products"].get_Product(st.session_state["var_columns"]).get_Keyword()+str(st.session_state["var_columns"])):
                    if st.session_state["cart"].add(st.session_state["products"].get_Product(st.session_state["var_columns"])):
                        st.write("Added to the cart!")
                    else:
                        st.write("Product already in the cart")
                        