import streamlit as st
from models.product_model import Product
from models.user_model import User

class Profile:
    def __init__(self) -> None:
        st.subheader("Welcome to your profile")
        column1,column2,column3 = st.columns(3,gap="small")
        st.subheader("My games:")
        column4,column5,column6 = st.columns(3,gap="small")
        with column1:
            st.image("./assets/joseph.jpg")
        with column2:
            if "userlogged" not in st.session_state:
                st.session_state["userlogged"] = st.session_state["username"]
                current_user = (f'{st.session_state["userlogged"]}')
            st.write(current_user)
            st.write()
            st.text("São Paulo, Brazil" )
            st.write("")
            st.write("")
            st.write("")
            st.text("No description.")
            st.write("")
            st.write("")
            st.text("🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮")
        with column3:
            st.write("")

        mygames = [
                    Product("Garry's Mod","Garry's Mod é um jogo sandbox de física.","10",25.99,"./assets/garrys.jpg"),
                    Product("Spore","Seja o arquiteto do seu próprio universo.","11",59.90,"./assets/spore.jpg"),
                    Product("Case: Animatronics","CASE: Animatronics é um desafiador e assustador jogo de terror furtivo","12",19.99,"./assets/case.jpg")
                    ]

        with column4:
            st.image(mygames[2].get_Image())
            st.text(mygames[2].get_Name())
        with column5:
            st.image(mygames[1].get_Image())
            st.text(mygames[1].get_Name())
        with column6:
            st.image(mygames[0].get_Image())
            st.text(mygames[0].get_Name())

        st.write("")
        st.title("Update here your email or password")
        st.write("")
        
        new_user_email = st.text_input("Enter your e-mail address:",key="new_user_email")
        if st.button("Update e-mail",key="change_email_button"):
            if st.session_state["users_db"].update_user(current_user, "e-mail", new_user_email):
                st.write("E-mail updated successfully")
            else:
                st.write("We couldn't update your e-mail, please try again later or verify your data.")                
        
        new_user_password = st.text_input("Enter new password:",key="new_user_password",type='password')
        if st.button("Change password",key="change_password_button"):
            if st.session_state["users_db"].update_user(current_user, "password", new_user_password):
                st.write("Password updated successfully")
            else:
                st.write("We couldn't update your password, please try again later or verify your data.")