class Tarefa:

    def __init__(self, descricao, concluida = False) -> None:
        self.descricao = descricao
        self.concluida = concluida
    
    def get_Descricao(self):
        return self._descricao

    def get_Concluida(self):
        return self._concluida

    def set_Concluida(self,status):
        self._concluida = status
    
    def __str__(self) -> str:
        return f'Tarefa[descricao: {self._descricao}] - concluida: {self._concluida}'