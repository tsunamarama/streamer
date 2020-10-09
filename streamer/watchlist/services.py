from streamer.adapters.repository import AbstractRepository
import streamer.utilities.services as util_services


def add_to_watchlist(movie_id: int, user_name: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    movie = repo.get_movie_by_id(movie_id)
    user.watchlist.add_movie(movie)


def get_watchlist(user_name: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    watchlist = user.watchlist
    return util_services.movies_to_dict(watchlist.watchlist)