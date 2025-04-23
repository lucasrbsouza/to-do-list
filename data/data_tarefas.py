from pathlib import Path
import json
from tarefas_model.tarefa import Tarefa
from tarefas_model.lista_de_Tarefas import ListaDeTarefa
def salvar(tarefa):
    path = Path("tarefa.json")
    contents = json.dumps(tarefa, indent=4)
    path.write_text(contents)


if __name__ == '__main__':
    tarefa1 = Tarefa(titulo="Trovejante", descricao="isso ai")
    tarefa2 = Tarefa(titulo="aaaaa", descricao="sdsds")
    tarefa = ListaDeTarefa()
    tarefa.adicionar(tarefa1)
    tarefa.adicionar(tarefa2)
    salvar(tarefa.to_dict())

    #preciso resolver esse problema