from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars0.githubusercontent.com/u/6677139?v=4"
    resp_mock.json.return_value = {
        "login": "smkbarbosa",
        "id": 6677139,
        "avatar_url": url
        }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('smkbarbosa')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('manus-consultoria')
    assert 'https://avatars2.githubusercontent.com/u/68953293?v=4' == url
