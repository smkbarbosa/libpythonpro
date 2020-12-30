from libpythonpro.spam.models import Usuario
from libpythonpro.tests.test_spam.conftest import conexao


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Samuel')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Samuel'), Usuario(nome='Dante')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

