import data_tarefas.data_tarefas as data
from tarefas_model.tarefa import Tarefa

def menu():
    lista_tarefa = data.carregar()

    while True:
        escolha = input("O que você quer fazer?\n"
                        "a) Criar tarefa\n"
                        "b) Listar tarefas\n"
                        "c) Deletar tarefas (em breve)\n"
                        "d) Concluir tarefa\n"
                        "e) Sair do programa\n> ")

        if escolha == "a":
            nome_tarefa = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            nova_tarefa = Tarefa(nome_tarefa.strip(), descricao.strip())
            lista_tarefa.adicionar(nova_tarefa)
            data.salvar(lista_tarefa.to_dict())
            print("--- Tarefa criada com sucesso! ---")

        elif escolha == "b":
            print("\n--- Lista de Tarefas ---")
            lista_tarefa.listar()

        elif escolha == "c":
            nome = input("Digite o nome da tarefa que deseja remover: ")
            data.remover(nome.strip())
            lista_tarefa = data.carregar()
            print(f"Tarefa '{nome}' removida com sucesso!")
            continue
        elif escolha == "d":
            nome = input("Digite o nome da tarefa a ser concluída: ")
            lista_tarefa.concluir(nome)
            data.salvar(lista_tarefa.to_dict())
            print("--- Tarefa marcada como concluída! ---")

        elif escolha == "e":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()