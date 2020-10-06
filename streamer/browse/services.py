from typing import List

from streamer.adapters.repository import AbstractRepository
from streamer.domain.model import Actor, Genre, Movie, Review


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass

"""
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
        'runtime': movie.runtime_minutes
    }


def movies_to_dict(movies: List[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def actor_to_dict(actor: Actor):
    return {
        'name': actor.actor_full_name
    }


def actors_to_dict(actors: List[Actor]):
    return [actor_to_dict(actor) for actor in actors]


def genre_to_dict(genre: Genre):
    return {
        'genre': genre.genre_type
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
    return [review_to_dict(review) for review in reviews]"""
