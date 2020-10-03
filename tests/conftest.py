import os
import pytest

from streamer import create_app
from streamer.adapters import memory_repository
from streamer.adapters.memory_repository import MemoryRepository


TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'marjo', 'iCloudDrive', 'University', 'COMPSCI 235', 'A2',
                              'streamer', 'tests', 'data')


@pytest.fixture
def test_repo():
    repo = MemoryRepository()
    memory_repository.load_data(TEST_DATA_PATH, repo)
    return repo


@pytest.fixture
def client():
    app = create_app({
        'TESTING': True,
        'TEST_DATA_PATH': TEST_DATA_PATH,
        'WTF_CSRF_ENABLED': False
    })
    return app.test_client()


class AuthManager:
    def __init__(self, client):
        self.__client = client

    def login(self, user_name='', password=''):
        return self.__client.post(
            'authentication/login',
            data={'username': user_name, 'password': password}
        )

    def logout(self):
        return self.__client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthManager(client)
