from streamer.adapters.repository import AbstractRepository
from flask import url_for
import streamer.utilities.services as util_services


def add_to_watchlist(movie_id: int, user_name: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    movie = repo.get_movie_by_id(movie_id)
    user.watchlist.add_movie(movie)


def remove_from_watchlist(movie_id: int, user_name: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    movie = repo.get_movie_by_id(movie_id)
    user.watchlist.remove_movie(movie)


def get_watchlist(user_name: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    watchlist = user.watchlist
    watchlist_dict = util_services.movies_to_dict(watchlist.watchlist)
    for movie in watchlist_dict:
        movie['rm_url'] = url_for('watchlist_bp.remove_from_watchlist', id=movie['id'])
        movie['review_url'] = url_for('review_bp.submit_review', id=movie['id'])
    return watchlist_dict
