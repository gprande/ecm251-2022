from item import Item
from carrinho import Carrinho

item1 = Item('Carregador', 'Carrega Iphone e Android', 200.0)
item2 = Item(
    valor = 350.0,
    nome = 'Stray',
    descricao = 'Gato'
)
item3 = Item(
    valor = 450.0,
    nome = 'Stray Deluxe',
    descricao = 'Gato de luxo'
)

carrinho = Carrinho()

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.adicionar(item1)
carrinho.adicionar(item2)

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.remover(item2)

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

