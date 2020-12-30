from libpythonpro.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Samuel', email='samuka1@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Samuel', email='samuka1@gmail.com'),
                Usuario(nome='Dante', email='samuka1@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
