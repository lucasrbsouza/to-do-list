# from tarefa import Tarefa
from tarefas_model import tarefa

class ListaDeTarefa:

    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
       self.tarefas.append(tarefa)

    def listar(self):
        for tarefa in self.tarefas:
            print(tarefa.imprimir())

    def remover(self, tarefa):
        self.tarefas.remove(tarefa)

    def concluir(self, nome_tarefa):
        for tarefa in self.tarefas:
            if tarefa.titulo == nome_tarefa:
                tarefa.is_concluida(nome_tarefa)

    def to_dict(self):
        return [tarefa.to_dict() for tarefa in self.tarefas]
if __name__ == '__main__':
    pass