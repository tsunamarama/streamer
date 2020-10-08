import streamer.utilities.services as util_services
from streamer.adapters.repository import AbstractRepository
from streamer.domain.model import Review


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_movie_reviews(movie_id: int, repo: AbstractRepository):
    movie = repo.get_movie_by_id(movie_id)
    if movie is None:
        raise NonExistentMovieException
    return util_services.reviews_to_dict(movie.reviews)


def get_movie_by_title(title: str, repo: AbstractRepository):
    return util_services.movie_to_dict(repo.get_movie_by_title(title))


def get_movie_reviews_by_title(title: str, repo: AbstractRepository):
    movie = repo.get_movie_by_title(title)
    reviews = repo.get_movie_reviews(movie)
    return util_services.reviews_to_dict(reviews)


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