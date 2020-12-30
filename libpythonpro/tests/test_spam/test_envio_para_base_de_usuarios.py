import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.models import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Samuel', email='samuka1@gmail.com'),
            Usuario(nome='Dante', email='contato@smkbarbosa.eti.br')
            ],
        [
            Usuario(nome='Samuel', email='samuka1@gmail.com')
            ]
        ]
    )
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'contato@smkbarbosa.eti.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
        )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Samuel', email='contato@smkbarbosa.eti.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'samuka1@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
        )
    assert enviador.parametros_de_envio == (
        'samuka1@gmail.com',
        'contato@smkbarbosa.eti.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
