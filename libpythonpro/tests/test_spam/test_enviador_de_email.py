import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['contato@smkbarbosa.eti.br', 'foo@bar.com.br']
    )
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'samuka1@gmail.com',
        'Curso Python Pro',
        'Turma Python Pro'
        )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
    )
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'samuka1@gmail.com',
            'Curso Python Pro',
            'Turma Python Pro'
            )
