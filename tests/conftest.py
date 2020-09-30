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
