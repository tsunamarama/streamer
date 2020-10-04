import os

from flask import Flask

import streamer.adapters.repository as repo
from streamer.adapters.memory_repository import MemoryRepository, load_data


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('covid', 'adapters', 'data')

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    load_data(data_path, repo.repo_instance)

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_bp)

        from .browse import browse
        app.register_blueprint(browse.browse_bp)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_bp)

        from .utilities import utilities
        app.register_blueprint(utilities.utilities_bp)

    return app
