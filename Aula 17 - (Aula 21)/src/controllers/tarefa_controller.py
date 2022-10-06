from models.tarefa import Tarefa

class TarefaController:

    def __init__(self) -> None:
        self._lista_de_tarefas = []
    
    def criar_Tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self._lista_de_tarefas.append(tarefa)

    def exibir_total_tarefas(self):
        return len(self._lista_de_tarefas)

    def exibir_tarefas_concluidas(self):
        total = 0
        for tarefa in self._lista_de_tarefas:
            if tarefa.get_Concluida():
                total += 1
        return total