from pathlib import Path
import json
from tarefas_model.tarefa import Tarefa
from tarefas_model.lista_de_Tarefas import ListaDeTarefa

def salvar(tarefa):
    path = Path("db_/tarefa.json")
    contents = json.dumps(tarefa, indent=4)
    path.write_text(contents)

def carregar():
    path = Path("db_/tarefa.json")
    if not path.exists():
        return ListaDeTarefa()

    contents = path.read_text()
    dados = json.loads(contents)

    lista = ListaDeTarefa()
    for item in dados:
        tarefa = Tarefa.from_dict(item)
        lista.adicionar(tarefa)

    return lista

def remover(nome_tarefa):
    lista = carregar()
    nova_lista = ListaDeTarefa()

    for tarefa in lista.tarefas:
        if tarefa.titulo != nome_tarefa:
            nova_lista.adicionar(tarefa)

    salvar(nova_lista.to_dict())



if __name__ == '__main__':
   pass