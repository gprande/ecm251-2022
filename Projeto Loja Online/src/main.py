import streamlit as st
from Modelos.item import Item
from Modelos.carrinho import Carrinho

if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = Carrinho()
if "joguitos" not in st.session_state:
    st.session_state["joguitos"] = [Item("Cities: Skylines","Cities: Skylines é uma versão moderna dos simuladores de cidade clássicos.","1",74.99,"./assets/cities.jpg"),
                                    Item("Phasmophobia","Phasmophobia é um jogo multijogador online (4 jogadores co-op) de terror psicológico.","2",27.90,"./assets/phasmo.png"),
                                    Item("Stardew Valley","Será que você vai aprender a viver da terra, a transformar esse matagal em um próspero lar?","3",24.99,"./assets/stardew.jpg"),
                                    Item("Devour","Corra. Grite. Esconda-se. Sobreviva a qualquer custo!","4",10.89,"./assets/devour.jpg"),
                                    Item("Rise of the Tomb Raider","Explore a Mansão Croft na nova história.","5",29.99,"./assets/rise.jpg"),
                                    Item("Dead by Daylight","DBD é um jogo em que você deve fugir do assassino e evitar ser pego.","6",49.99,"./assets/dbd.jpg"),
                                    Item("Minecraft Bedrock & Java Edition","Minecraft Launcher é seu portal para o universo do Minecraft","7",129.00,"./assets/mine.jpg"),
                                    Item("PowerWash Simulator","Se livre de preocupações com os sons suaves de água em alta pressão.","8",74.90,"./assets/power.jpg"),
                                    Item("Forza Horizon 5","Explore o mundo aberto vibrante em terras mexicanas.","9",249.00,"./assets/forza.jpg")]

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
            #del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input(label="Usuário", key="username")
        st.text_input(label="Senha", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci a senha"):
                st.write("Aguarde...")
        return False
    
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(label="Usuário", key="username")
        st.text_input(label="Senha", type="password", key="password")
        col1,col2 = st.columns(spec=[1,10],gap="small")
        with col1:    
            if st.button(label="Login"):
                password_entered()
        with col2:
            if st.button(label="Esqueci minha senha"):
                st.write("Aguarde")    
        st.error("Senha incorreta")
        return False
    
    else:
        # Password correct.
        return True

if check_password():
    store,cart = st.tabs(["Loja","Carrinho"])    
    with store:
        st.subheader("Destaques")
        c1,c2,c3 = st.columns(3,gap="small")
        c4,c5,c6 = st.columns(3,gap="small")
        c7,c8,c9 = st.columns(3,gap="small")
        colunas = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        var = 0
        for coluna in colunas:
            with coluna:
                st.image(st.session_state["joguitos"][var].get_Imagem(), st.session_state["joguitos"][var].get_Descricao())
                st.write("R$ "+ str(st.session_state["joguitos"][var].get_Valor()))
                if st.button("Adicionar ao carrinho", key = st.session_state["joguitos"][var].get_Chave()):
                    st.session_state["carrinho"].adicionar(st.session_state["joguitos"][var])
                    st.write("Produto adicionado ao carrinho")
                var += 1        
    with cart:
        col1,col2,col3 = st.columns([1.5,5,2.5],gap = "small")
        with col1:
            st.write("Remover:")
            contador = 0
            while contador < st.session_state["carrinho"].get_Quantidade_Itens():
                aux = st.session_state["carrinho"].exibir_Itens(contador)
                if st.button("Remover",key = ("Remover_"+aux.get_Chave()+str(contador))):
                    st.session_state["carrinho"].remover(aux)
                contador += 1        
        with col2:
            st.write("Itens:")
            i = 0
            while i < st.session_state["carrinho"].get_Quantidade_Itens():
                st.write(str(st.session_state["carrinho"].exibir_Itens(i)))
                st.text(" ")
                i+=1
        with col3:
            st.write("Resumo da Compra:")
            st.write("Quant. de itens: "+str(st.session_state["carrinho"].get_Quantidade_Itens()))
            st.write("Valor total: R$ "+str(st.session_state["carrinho"].get_Valor_Total()))
            if st.button("Pagamento",key = ("pagamento")):
                st.write("Aguarde")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)