import streamlit as st
from Modelos.item import Item
from Modelos.carrinho import Carrinho

joguitos = [
Item("Cities: Skylines","Cities: Skylines é uma versão moderna dos simuladores de cidade clássicos.",74.99,"./assets/cities.png"),
Item("Phasmophobia","Phasmophobia é um jogo multijogador online (4 jogadores co-op) de terror psicológico.",27.90,"./assets/phasmo.png"),
Item("Stardew Valley","Será que você vai aprender a viver da terra, a transformar esse matagal em um próspero lar?",24.99,"./assets/stardew.jpg"),
Item("Devour","Corra. Grite. Esconda-se. Sobreviva a qualquer custo!",10.89,"./assets/devour.jpg"),
Item("Rise of the Tomb Raider","Explore a Mansão Croft na nova história “Laços de Sangue” e a defenda contra uma invasão zumbi em “Pesadelo de Lara”.",29.99,"./assets/rise.jpg"),
Item("Dead by Daylight","DBD é um jogo multijogador de terror em que você deve fugir do assassino e evitar ser pego e morto.",49.99,"./assets/dbd.jpg"),
Item("Minecraft Bedrock & Java Edition","Minecraft Launcher é seu portal para o universo do Minecraft",129.00,"./assets/mine.jpg"),
Item("PowerWash Simulator","Se livre de preocupações com os sons suaves de água em alta pressão.",74.90,"./assets/power.jpg"),
Item("Forza Horizon 5","Sua maior aventura Horizon te espera! Explore o mundo aberto vibrante e em constante evolução nas terras mexicanas.",249.00,"./assets/forza.jpg")]

st.set_page_config(page_title="Prandelitz Store",layout="centered",initial_sidebar_state="collapsed",menu_items=None)

def check_password():
    """Returns `True` if the user had a correct password."""
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input(label="Digite seu E-mail:", key="username")
        st.text_input(label="Digite sua Senha:", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Redirecionando...")
        return False
    
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(label="Digite seu E-mail:", key="username")
        st.text_input(label="Digite sua Senha:", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Calma aew, to no processo aqui...")
            # Botão sem função por enquanto, aguarde novas atualizações...    
        st.error("ERRROUUU 🤣")
        return False
    
    else:
        # Password correct.
        return True

if check_password():
    home,carrinho = st.tabs(["Home","Carrinho"])
    
    with home:
        st.subheader("Destaques")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        var = 0
        prod_key_1 = "Produto_"
        for i in colunas:
            with i:
                prod_key_2 = str(var)
                prod_key = prod_key_1+prod_key_2
                st.image(joguitos[var].get_Imagem(),joguitos[var].get_Valor())
                if st.button("Adicionar ao carrinho",key=prod_key):
                    carrinho.adicionar(joguitos[var])
                var += 1
    
    with carrinho:
        col1,col2 = st.columns([2,1],gap = "small")
        with col1:
            st.write("Itens:")
            st.write(str(carrinho.exibir_Itens()))
        with col2:
            st.write("Resumo da Compra:")
            st.write(str(carrinho.get_Quantidade_Itens()))
            st.write(str(carrinho.get_Valor_Total()))

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)