class Carrinho():
    # Método construtor
    def __init__(self):
        self._itens = []

    # Demais métodos da classe

    def get_Valor_Total(self):
        total = 0.0
        for item in self._itens:
            total += item.get_Valor()
        return total

    def get_Quantidade_Itens(self):
        return len(self._itens)

    def adicionar(self,item):
        self._itens.append(item)

    def remover(self,item):
        if item in self._itens:
            self._itens.remove(item)
            
    def get_Quantidade_Itens_Repetidos(self,objetivo):
        contador = 0
        for item in self._itens:
            if objetivo == item:
                contador += 1
        return contador

    def exibir_Itens(self,item):
        return self._itens[item]
    