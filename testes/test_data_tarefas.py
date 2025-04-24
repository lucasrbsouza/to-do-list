import pytest
import json
from unittest.mock import patch

from tarefas_model.tarefa import Tarefa
from tarefas_model.lista_de_Tarefas import ListaDeTarefa
from data_tarefas.data_tarefas import salvar, carregar, remover


@pytest.fixture
def lista_exemplo():
    lista = ListaDeTarefa()
    lista.adicionar(Tarefa("Tarefa 1", "Descrição 1"))
    lista.adicionar(Tarefa("Tarefa 2", "Descrição 2", True))
    return lista


def test_salvar(lista_exemplo):
    """Testa se a função salvar grava corretamente no arquivo JSON"""
    mock_data = json.dumps(lista_exemplo.to_dict(), indent=4)

    with patch('pathlib.Path.write_text') as mock_write:
        salvar(lista_exemplo.to_dict())
        mock_write.assert_called_once_with(mock_data)


def test_carregar_arquivo_existente():
    """Testa o carregamento quando o arquivo existe"""
    mock_content = json.dumps([
        {"titulo": "Tarefa 1", "descricao": "Desc 1", "concluida": False},
        {"titulo": "Tarefa 2", "descricao": "Desc 2", "concluida": True}
    ])

    with patch('pathlib.Path.exists', return_value=True), \
            patch('pathlib.Path.read_text', return_value=mock_content):
        lista = carregar()

        assert len(lista.tarefas) == 2
        assert lista.tarefas[0].titulo == "Tarefa 1"
        assert lista.tarefas[1].concluida is True


def test_carregar_arquivo_inexistente():
    """Testa o carregamento quando o arquivo não existe"""
    with patch('pathlib.Path.exists', return_value=False):
        lista = carregar()
        assert isinstance(lista, ListaDeTarefa)
        assert len(lista.tarefas) == 0