import streamlit as st
from visual.register import Register
from controllers.user_controller import UserController

# Retorns 'True' if user/password was spelled correctly.
def Login():
    st.session_state["users_db"] = UserController()
    if "login_true" not in st.session_state:
        st.session_state["login_true"] = False
    
    def password_entered():
        # Check if user/password is correct.
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"] == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            st.session_state["login_true"] = True
            # Deletes the used password of current session_state.
            del st.session_state["password"]  
            # del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False
    
    login,register = st.tabs(["Home Page","Register here"])
    
    if (st.session_state["login_true"] != True):
        with register:
            Register()
    else: 
        with register:
            st.write("Logged in")
    
    with login:
        if "password_correct" not in st.session_state:
            # Inictialization, shows fields for entering username/password.
            st.text_input(label="Enter your username:", 
                          key="username", 
                          placeholder = "Enter your user or e-mail address(no domain)")
            st.text_input(label="Enter your password:", type="password", key="password")  
            if st.button(label="Login"):
                password_entered()
            return False
        
        elif not st.session_state["password_correct"]:
            # Wrong password - shows error message and allows password to be entered again.
            st.text_input(label="Enter your username:", 
                          key="username",
                          placeholder = "Enter your user or e-mail address(no domain)")
            st.text_input(label="Enter your password:", type="password", key="password")  
            if st.button(label="Login"):
                password_entered()
            st.error("Wrong password/username")
            return False
        else:
            # if the password is right.
            return True