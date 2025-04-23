# from tarefa import Tarefa

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

    def concluir(self, tarefa):
        tarefa.is_concluida()
    def to_dict(self):
        return [tarefa.to_dict() for tarefa in self.tarefas]
if __name__ == '__main__':
    pass
# temos que passar essa classe para salvar em um json