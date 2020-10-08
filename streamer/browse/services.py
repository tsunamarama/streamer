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


def movies_to_dict(movies: List[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def movie_to_dict(movie: Movie):
    return {
        'id': movie.movie_id,
        'title': movie.title
    }


"""
def get_movies_by_genre(genre: Genre, repo: AbstractRepository):
    movies = repo.get_movies_by_genre(genre)
    return util_services.movies_to_dict(movies)
"""


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


"""from typing import List

from streamer.adapters.repository import AbstractRepository
from streamer.domain.model import Actor, Director, Genre, Movie, Review
import tmdbsimple as tmdb


tmdb.API_KEY = '241b1bfaa14ca0413e6776a613e381b6'
base_url = tmdb.Configuration().info()['images']['base_url']
# size = 'original'
size = 'w500'


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def add_review(movie_id: int, review_text: str, rating: int, user_name: str, repo: AbstractRepository):
    movie = repo.get_movie_by_id(movie_id)
    if movie is None:
        raise NonExistentMovieException
    user = repo.get_user(user_name)
    if user is None:
        raise UnknownUserException
    review = Review(
        movie=movie,
        review_text=review_text,
        rating=rating,
        user=user
    )
    repo.add_review(review)


def get_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie_by_id(movie_id)
    if movie is None:
        raise NonExistentMovieException
    return movie_to_dict(movie)


def get_movies_by_genre(genre: Genre, repo: AbstractRepository):
    movies = repo.get_movies_by_genre(genre)
    return movies_to_dict(movies)


def get_movies_by_id(id_list: list, repo: AbstractRepository):
    movies = repo.get_movies_by_id(id_list)
    return movies_to_dict(movies)


def get_reviews_for_movie(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie_by_id(movie_id)
    if movie is None:
        raise NonExistentMovieException
    return reviews_to_dict(movie.reviews)


def get_genre_movies(genre_id: int, repo: AbstractRepository):
    genre = repo.get_genre_by_id(genre_id)
    movies = repo.get_movies_by_id(genre.movies)
    return movies_to_dict(movies)


def get_director_movies(director_id: int, repo: AbstractRepository):
    director = repo.get_director_by_id(director_id)
    return movies_to_dict(director.movies)


def get_actor_movies(actor_id: int, repo: AbstractRepository):
    actor = repo.get_actor_by_id(actor_id)
    return movies_to_dict(actor.movies)


def get_movie_poster_url(movie: Movie):
    if movie.poster_url == '':
        response = tmdb.Search().movie(query=movie.title)
        if response['total_results'] > 0:
            poster_path = response['results'][0]['poster_path']
            if poster_path is not None:
                movie.poster_url = base_url + size + poster_path
                return movie.poster_url
            else:
                return None
    else:
        return movie.poster_url


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
        'poster_url': get_movie_poster_url(movie)
    }


def movies_to_dict(movies: List[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def actor_to_dict(actor: Actor):
    return {
        'id': actor.actor_id,
        'name': actor.actor_full_name,
        'movies': movies_to_dict(actor.movies)
    }


def actors_to_dict(actors: List[Actor]):
    return [actor_to_dict(actor) for actor in actors]


def genre_to_dict(genre: Genre):
    return {
        'id': genre.genre_id,
        'genre': genre.genre_type,
        'movies': movies_to_dict(genre.movies)
    }


def genres_to_dict(genres: List[Genre]):
    return [genre_to_dict(genre) for genre in genres]


def review_to_dict(review: Review):
    return {
        'movie': review.movie,
        'review_text': review.review_text,
        'rating': review.rating,
        'timestamp': review.timestamp,
        'user': review.user.user_name
    }


def reviews_to_dict(reviews: List[Review]):
    return [review_to_dict(review) for review in reviews]


def director_to_dict(director: Director):
    return {
        'id': director.director_id,
        'name': director.director_full_name,
        'movies': movies_to_dict(director.movies)
    }"""
