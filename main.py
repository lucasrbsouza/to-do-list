from json import JSONDecodeError
import typer

import data_tarefas.data_tarefas as data
from tarefas_model.tarefa import Tarefa

app = typer.Typer()

@app.command()
def criar_tarefa(titulo: str, descricao: str):
    """
    Cria uma nova tarefa.
    (ex: criar-tarefa "titulo" "descricao")
    """
    try:
        lista_tarefa = data.carregar()
        nova_tarefa = Tarefa(titulo.strip(), descricao)
        lista_tarefa.adicionar(nova_tarefa)
        data.salvar(lista_tarefa.to_dict())
        print("--- Tarefa criada com sucesso! ---")
    except Exception as e:
        print(f"erro inesperado: {e}")
    except JSONDecodeError as e:
        print(f"erro com arquivo: {e}")

@app.command()
def listar_tarefas():
    """
    Lista todas as tarefas.
    (ex: listar-tarefas)
    """
    try:
        lista_tarefa = data.carregar()
        if not lista_tarefa.tarefas:
            print("\n--- Nenhuma tarefa encontrada! ---")
        else:
            print("\n--- Lista de Tarefas ---")
            lista_tarefa.listar()
    except JSONDecodeError:
        print("\n--- Erro ao listar tarefas! O arquivo de dados está corrompido. ---")
    except Exception as e:
        print(f"\n--- Erro inesperado: {e} ---")

@app.command()
def deletar_tarefa(nome: str):
    """
    Remove uma tarefa.
    (ex: deletar-tarefa "nome da tarefa")
    """
    try:
        data.remover(nome.strip())
        lista_tarefa = data.carregar()
        print(f"Tarefa '{nome}' removida com sucesso!")
    except Exception as e:
        print(f"Erro ao remover tarefa: {e}")
    except JSONDecodeError:
        print("\n--- Erro ao deletar tarefa! O arquivo de dados deve está corrompido. ---")

@app.command()
def concluir_tarefa(nome: str):
    """
    Marca uma tarefa como concluída.
    (ex: concluir-tarefa "nome da tarefa")
    """
    try:
        lista_tarefa = data.carregar()
        lista_tarefa.concluir(nome)
        data.salvar(lista_tarefa.to_dict())
        print("--- Tarefa marcada como concluída! ---")
    except Exception as e:
        print(f"Erro ao concluir tarefa: {e}")
    print("\n--- Erro ao concluir tarefa! O arquivo de dados deve está corrompido. ---")

if __name__ == "__main__":
    app()
