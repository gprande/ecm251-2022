import streamlit as st
from controllers.user_controller import UserController

def accept_register(new_user,new_email,new_password,new_cpf,new_birthdate,new_username):
    if st.session_state["users_db"].add_user(new_user,
                                            new_email,
                                            new_password,
                                            new_cpf,
                                            new_birthdate,
                                            new_username):
        st.write("Registered successfully")
    else:
        st.write("Não foi possível realizar o cadastro, por favor, verifique seus dados.")

class Register():
    def __init__(self) -> None:       
        new_username = st.text_input(label="Enter your name", key="new_username")
        new_birthdate = st.text_input(label="Enter your birthdate", key="new_birthdate")
        new_cpf = st.text_input(label="Enter your CPF (Only numbers):", key="new_cpf")
        new_user = st.text_input(label="Enter your desired username :", key="new_user")
        new_email = st.text_input(label="Enter your e-mail adress", key="new_email")
        new_password = st.text_input(label="Type your desired password",type="password", key="new_password")
        
        if st.button("Register", key="register_button"):
            accept_register(new_user,
                            new_email,
                            new_password,
                            new_cpf,
                            new_birthdate,
                            new_username)