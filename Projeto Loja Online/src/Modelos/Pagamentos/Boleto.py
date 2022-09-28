from datetime import date
from random import random

class Boleto(Pagamento):
    def __init__(self, valor, dias_p_vencimento = 0):
        self._valor = valor
        self._vencimento = date.today() + dias_p_vencimento

    def realizar_pagamento(self):
        return True

    def gerar_codigo_boleto(self):
        return f"8400{self._vencimento}{self._valor}"
