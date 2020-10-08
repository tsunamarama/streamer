import os

from flask import Flask

import streamer.adapters.repository as repo
from streamer.adapters.memory_repository import MemoryRepository, load_data


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path = os.path.join('streamer', 'adapters', 'data')
    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']
    repo.repo_instance = MemoryRepository()
    load_data(data_path, repo.repo_instance)
    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_bp)
        from .browse import browse
        app.register_blueprint(browse.browse_bp)
        from .movie import movie
        app.register_blueprint(movie.movie_bp)
        from .authentication import authentication
        app.register_blueprint(authentication.authentication_bp)
        from .utilities import utilities
        app.register_blueprint(utilities.utilities_bp)
    return app
