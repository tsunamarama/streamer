from flask import url_for
from typing import List
from streamer.adapters.repository import AbstractRepository
from streamer.domain.model import Movie
import streamer.utilities.services as util_services


def get_genre_subtitle(genre_id: int, repo: AbstractRepository):
    genre = repo.get_genre_by_id(genre_id)
    return 'Showing results for the ' + genre.genre_type + ' genre'


def get_actor_subtitle(actor_id: int, repo: AbstractRepository):
    actor = repo.get_actor_by_id(actor_id)
    return 'Showing results for ' + actor.actor_full_name


def get_director_subtitle(director_id: int, repo: AbstractRepository):
    director = repo.get_director_by_id(director_id)
    return 'Showing results for ' + director.director_full_name


def get_movie_subtitle(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie_by_id(movie_id)
    return 'Showing results for ' + movie.title


def get_genre_labels(repo: AbstractRepository):
    genres = repo.get_genres()
    genres.sort()
    genres_dict = util_services.genres_to_dict(genres)
    for genre in genres_dict:
        genre['url'] = url_for('browse_bp.browse_by_genre', id=genre['id'])
    return genres_dict


def get_actor_labels(repo: AbstractRepository):
    actors = repo.get_actors()
    actors.sort()
    actors_dict = util_services.actors_to_dict(actors)
    for actor in actors_dict:
        actor['url'] = url_for('browse_bp.browse_by_actor', id=actor['id'])
    return actors_dict


def get_director_labels(repo: AbstractRepository):
    directors = repo.get_directors()
    directors.sort()
    directors_dict = util_services.directors_to_dict(directors)
    for directors in directors_dict:
        directors['url'] = url_for('browse_bp.browse_by_director', id=directors['id'])
    return directors_dict


def get_movie_labels(repo: AbstractRepository):
    movies = repo.get_movies()
    movies.sort()
    movies_dict = movies_to_dict(movies)
    for movies in movies_dict:
        movies['url'] = url_for('movie_bp.movie_by_id', id=movies['id'])
    return movies_dict


def get_genre_batch_dict(genre_id: int, repo: AbstractRepository, limit=9):
    genre = repo.get_genre_by_id(genre_id)
    movies = repo.get_movies_by_genre(genre)
    batch_list = [movies[i:i + limit] for i in range(0, len(movies), limit)]
    for batch in batch_list:
        util_services.movies_to_dict(batch)
    return batch_list


def movies_to_dict(movies: List[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def movie_to_dict(movie: Movie):
    return {
        'id': movie.movie_id,
        'title': movie.title
    }


def get_genre_movies(genre_id: int, repo: AbstractRepository):
    genre = repo.get_genre_by_id(genre_id)
    movies = repo.get_movies_by_genre(genre)
    return util_services.movies_to_dict(movies)


def get_actor_movies(actor_id: int, repo: AbstractRepository):
    actor = repo.get_actor_by_id(actor_id)
    movies = repo.get_movies_by_actor(actor)
    return util_services.movies_to_dict(movies)


def get_director_movies(director_id: int, repo: AbstractRepository):
    director = repo.get_director_by_id(director_id)
    movies = repo.get_movies_by_director(director)
    return util_services.movies_to_dict(movies)
