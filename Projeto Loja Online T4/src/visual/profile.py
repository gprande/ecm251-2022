import streamlit as st

class Profile:
    def __init__(self) -> None:
        if "userlogged" not in st.session_state:
            st.session_state["userlogged"] = st.session_state["username"]
        current_user = (f'{st.session_state["userlogged"]}')
        
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