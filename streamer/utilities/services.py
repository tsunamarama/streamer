import random

from streamer.adapters.repository import AbstractRepository
from streamer.domain.movie import Movie
from streamer.domain.genre import Genre
from typing import List


def get_genre_labels(repo: AbstractRepository) -> List[Genre]:
    return repo.get_genres()


def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = len(repo.get_movies())
    random_ids = random.sample(range(1, movie_count), quantity)
    movies = repo.get_movies_by_id(random_ids)
    return movies_to_dict(movies)


def movie_to_dict(movie: Movie):
    return {
        'title': movie.title,
        'year': movie.year,
        'actors': movie.actors,
        'director': movie.director,
        'runtime': movie.runtime_minutes,
        'genres': movie.genres
    }


def movies_to_dict(movies: List[Movie]):
    return [movie_to_dict(movie) for movie in movies]

