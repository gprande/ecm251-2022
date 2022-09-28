from cgi import print_exception
from unicodedata import name


class Item():
    def __init__(self,nome,descricao,chave,preco,imagem) -> None:
        self._nome = nome
        self._descricao = descricao
        self._chave = chave
        self._preco = preco 
        self._imagem = imagem
    # Faz com que o item print de forma especifica
    def __str__(self) -> str:
        return f'Item(nome):{self._nome},descricao:{self._descricao} preco:{self._preco}, imagem:{self._imagem}'
    #Compara itens
    def __eq__(self, __o: object) -> bool:
        if(isinstance(__o,Item)):
            return self._nome == __o.get_Nome()
        return False
    # Getters da classe
    def get_Nome(self):
        return self._nome
    def get_Descricao(self):
        return self._descricao
    def get_chave(self):
        return self._chave
    def get_Valor(self):
        return self._preco
    def get_Imagem(self):
        return self._imagem