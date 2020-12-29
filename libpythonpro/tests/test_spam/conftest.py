import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='module')
def conexao():
    # SETUP
    conexao_obj = Conexao()
    # yield retorna o valor que será injetado no teste
    yield conexao_obj
    # tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
