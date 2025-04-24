import pytest
from tarefas_model.tarefa import Tarefa

@pytest.fixture
def tarefa_nao_concluida():
    return Tarefa(titulo="Estudar Python", descricao="Estudar pytest e TDD")

@pytest.fixture
def tarefa_concluida():
    tarefa = Tarefa(titulo="Fazer compras", descricao="Leite e ovos")
    tarefa.is_concluida("Fazer compras")
    return tarefa

def test_criacao_tarefa(tarefa_nao_concluida):
    """Testa a inicialização correta de uma tarefa"""
    assert tarefa_nao_concluida.titulo == "Estudar Python"
    assert tarefa_nao_concluida.descricao == "Estudar pytest e TDD"
    assert tarefa_nao_concluida.concluida is False

def test_marcar_como_concluida(tarefa_nao_concluida):
    """Testa se uma tarefa pode ser marcada como concluída"""
    tarefa_nao_concluida.is_concluida("Estudar Python")
    assert tarefa_nao_concluida.concluida is True

def test_imprimir_tarefa_nao_concluida(tarefa_nao_concluida):
    """Testa a representação em string de tarefa não concluída"""
    assert tarefa_nao_concluida.imprimir() == "[ ] Estudar Python - Estudar pytest e TDD"

def test_imprimir_tarefa_concluida(tarefa_concluida):
    """Testa a representação em string de tarefa concluída"""
    assert tarefa_concluida.imprimir() == "[X] Fazer compras - Leite e ovos"

def test_to_dict_nao_concluido(tarefa_nao_concluida):
    """Testa a conversão para dicionário de tarefa não concluída"""
    expected = {
        "titulo": "Estudar Python",
        "descricao": "Estudar pytest e TDD",
        "concluida": False
    }
    assert tarefa_nao_concluida.to_dict() == expected

def test_to_dict_concluido(tarefa_concluida):
    """Testa a conversão para dicionário de tarefa concluída"""
    expected = {
        "titulo": "Fazer compras",
        "descricao": "Leite e ovos",
        "concluida": True
    }
    assert tarefa_concluida.to_dict() == expected

def test_from_dict():
    """Testa a criação de tarefa a partir de dicionário"""
    data = {
        "titulo": "Ler livro",
        "descricao": "Ler Clean Code",
        "concluida": True
    }
    tarefa = Tarefa.from_dict(data)
    assert tarefa.titulo == "Ler livro"
    assert tarefa.descricao == "Ler Clean Code"
    assert tarefa.concluida is True

def test_from_dict_sem_status():
    """Testa criação a partir de dicionário sem status (deve usar False como padrão)"""
    data = {
        "titulo": "Exercícios",
        "descricao": "Fazer exercícios físicos"
    }
    tarefa = Tarefa.from_dict(data)
    assert tarefa.concluida is False

def test_marcar_concluida_com_nome_diferente(tarefa_nao_concluida):
    """Testa que marcar como concluída funciona mesmo com nome diferente do parâmetro"""
    tarefa_nao_concluida.is_concluida("Nome diferente")
    assert tarefa_nao_concluida.concluida is True