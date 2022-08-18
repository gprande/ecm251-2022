from mimetypes import init


class Cartao(Pagamento):
    def __init__(self, numero, titular, validade, cvv):
        self._numero = numero
        self._titular = titular
        self._validade = validade
        self._cvv = cvv

    def get_titular(self):
        return self._titular

    def get_validade(self):
        return self._validade

    def get_numero(self):
        return self._numero[len(self._numero) - 4:]   