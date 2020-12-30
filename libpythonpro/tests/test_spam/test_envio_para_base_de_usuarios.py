import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.models import Usuario


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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'contato@smkbarbosa.eti.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
        )
    assert len(usuarios) == enviador.qtd_email_enviados
