from flask import Blueprint, url_for
import streamer.adapters.repository as repo
import streamer.utilities.services as services
import streamer.movie.services as mov_services


utilities_bp = Blueprint('utilities_bp', __name__)


def get_selected_movies(quantity=9):
    movies = services.get_random_movies(quantity, repo.repo_instance)
    return movies


def get_selected_movie(movie_title: str):
    movie = mov_services.get_movie_by_title(movie_title, repo.repo_instance)
    movie['url'] = url_for('movie_bp.movie_by_title', title=movie['title'])
    return movie


def get_selected_movie_by_id(movie_id: int):
    return services.get_movie(movie_id, repo.repo_instance)


def get_selected_movie_by_title(title: str):
    return mov_services.get_movie_by_title(title, repo.repo_instance)


def get_selected_movie_reviews_by_id(movie_id: int):
    return mov_services.get_movie_reviews(movie_id, repo.repo_instance)


def get_selected_movie_reviews_by_title(title: str):
    return mov_services.get_movie_reviews_by_title(title, repo.repo_instance)
