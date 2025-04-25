import pytest
from tarefas_model.lista_de_Tarefas import ListaDeTarefa
from tarefas_model.tarefa import Tarefa


@pytest.fixture
def lista_tarefas():
    return ListaDeTarefa()

@pytest.fixture
def tarefa_exemplo():
    return Tarefa(titulo="Tarefa de exemplo", descricao="Descrição de exemplo")


def test_adicionar_tarefa(lista_tarefas, tarefa_exemplo):
    lista_tarefas.adicionar(tarefa_exemplo)
    assert len(lista_tarefas.tarefas) == 1
    assert lista_tarefas.tarefas[0] == tarefa_exemplo


def test_listar_tarefas(lista_tarefas, tarefa_exemplo, capsys):
    lista_tarefas.adicionar(tarefa_exemplo)
    lista_tarefas.listar()
    captured = capsys.readouterr()
    assert "[ ] Tarefa de exemplo - Descrição de exemplo" in captured.out


def test_remover_tarefa(lista_tarefas, tarefa_exemplo):
    lista_tarefas.adicionar(tarefa_exemplo)
    assert len(lista_tarefas.tarefas) == 1
    lista_tarefas.remover(tarefa_exemplo)
    assert len(lista_tarefas.tarefas) == 0


def test_concluir_tarefa(lista_tarefas, tarefa_exemplo, mocker):
    # Testa se is_concluida é chamado quando concluímos via ListaDeTarefa
    spy = mocker.spy(tarefa_exemplo, 'is_concluida')
    lista_tarefas.adicionar(tarefa_exemplo)
    lista_tarefas.concluir("Tarefa de exemplo")

    # Verifica se o método foi chamado
    spy.assert_called_once_with("Tarefa de exemplo")
    assert tarefa_exemplo.concluida is True


def test_to_dict(lista_tarefas, tarefa_exemplo):
    lista_tarefas.adicionar(tarefa_exemplo)
    result = lista_tarefas.to_dict()
    expected = [{
        "titulo": "Tarefa de exemplo",
        "descricao": "Descrição de exemplo",
        "concluida": False
    }]
    assert result == expected


def test_concluir_tarefa_inexistente(lista_tarefas, tarefa_exemplo):
    lista_tarefas.adicionar(tarefa_exemplo)
    # Tenta concluir tarefa que não existe
    lista_tarefas.concluir("Tarefa inexistente")
    # Verifica que a tarefa existente não foi marcada como concluída
    assert tarefa_exemplo.concluida is False


def test_listar_tarefa_concluida(lista_tarefas, tarefa_exemplo, capsys):
    tarefa_exemplo.is_concluida("Tarefa de exemplo")  # Marca como concluída
    lista_tarefas.adicionar(tarefa_exemplo)
    lista_tarefas.listar()
    captured = capsys.readouterr()
    assert "[X] Tarefa de exemplo - Descrição de exemplo" in captured.out