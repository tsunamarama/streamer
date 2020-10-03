from flask import Blueprint, url_for

import streamer.adapters.repository as repo
import streamer.utilities.services as services


utilities_bp = Blueprint('utilities_bp', __name__)


def get_selected_movies(quantity=3):
    movies = services.get_random_movies(quantity, repo.repo_instance)
    for movie in movies:
        pass