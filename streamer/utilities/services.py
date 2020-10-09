import random
from flask import url_for
from streamer.adapters.repository import AbstractRepository
from streamer.domain.model import Actor, Director, Genre, Movie, Review, User, WatchList
from typing import List
import tmdbsimple as tmdb


class NonExistentMovieException(Exception):
    pass


tmdb.API_KEY = '241b1bfaa14ca0413e6776a613e381b6'
base_url = tmdb.Configuration().info()['images']['base_url']
# size = 'original'
size = 'w500'


def get_movie_poster_url(movie: Movie):
    if movie.poster_url == '':
        response = tmdb.Search().movie(query=movie.title)
        if response['total_results'] > 0:
            poster_path = response['results'][0]['poster_path']
            if poster_path is not None:
                movie.poster_url = base_url + size + poster_path
                return movie.poster_url
            else:
                movie.poster_url = 'static/images/default.png'
                return movie.poster_url
    else:
        return movie.poster_url


def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = len(repo.get_movies())
    random_ids = random.sample(range(1, movie_count), quantity)
    movies = repo.get_movies_by_rank(random_ids)
    movies_dict = movies_to_dict(movies)
    return movies_dict


def get_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie_by_id(movie_id)
    if movie is None:
        raise NonExistentMovieException
    return movie_to_dict(movie)


def get_movies_by_id(id_list: list, repo: AbstractRepository):
    movies = repo.get_movies_by_id(id_list)
    return movies_to_dict(movies)


def movie_to_dict(movie: Movie):
    return {
        'id': movie.movie_id,
        'title': movie.title,
        'year': movie.year,
        'desc': movie.description,
        'director': movie.director,
        'actors': actors_to_dict(movie.actors),
        'genres': genres_to_dict(movie.genres),
        'reviews': reviews_to_dict(movie.reviews),
        'runtime': movie.runtime_minutes,
        'poster_url': get_movie_poster_url(movie),
        'url': url_for('movie_bp.movie_by_id', id=movie.movie_id)
    }


def director_to_dict(director: Director):
    return {
        'id': director.director_id,
        'name': director.director_full_name,
    }


def directors_to_dict(directors: List[Director]):
    return [director_to_dict(director) for director in directors]


def movies_to_dict(movies: List[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def actor_to_dict(actor: Actor):
    return {
        'id': actor.actor_id,
        'name': actor.actor_full_name
    }


def actors_to_dict(actors: List[Actor]):
    return [actor_to_dict(actor) for actor in actors]


def genre_to_dict(genre: Genre):
    return {
        'id': genre.genre_id,
        'genre': genre.genre_type
    }


def genres_to_dict(genres: List[Genre]):
    return [genre_to_dict(genre) for genre in genres]


def user_to_dict(user: User):
    return {
        'id': user.user_id,
        'username': user.user_name,
        'password': user.password,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'watched_movies': movies_to_dict(user.watched_movies),
        'reviews': reviews_to_dict(user.reviews),
        'time_spent_watching': user.time_spent_watching_movies_minutes,
        'watchlist': watchlist_to_dict(user.watchlist)
    }


def review_to_dict(review: Review):
    return {
        'movie': review.movie,
        'review_text': review.review_text,
        'rating': review.rating,
        'timestamp': review.timestamp.strftime("%d %B %Y"),
        'user': review.user
    }


def reviews_to_dict(reviews: List[Review]):
    return [review_to_dict(review) for review in reviews]


def watchlist_to_dict(watchlist: WatchList):
    return {
        'watchlist': movies_to_dict(watchlist.watchlist)
    }
