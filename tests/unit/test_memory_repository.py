import pytest

from streamer.adapters.repository import AbstractRepository
from streamer.domain.actor import Actor
from streamer.domain.director import Director
from streamer.domain.genre import Genre
from streamer.domain.movie import Movie
from streamer.domain.review import Review
from streamer.domain.user import User

from streamer.adapters.repository import RepositoryException


def test_repository_add_user(test_repo):
    user = User(
        user_name='mjoh781@aucklanduni.ac.nz',
        password='cassia',
        first_name='Michael',
        last_name='Johnson',
        user_id=4
    )
    test_repo.add_user(user)
    assert test_repo.get_user_by_id(4) is user


def test_repository_get_user_by_id(test_repo):
    user = test_repo.get_user_by_id(1)
    assert user.user_name == 'm.a.r.johnson@me.com'


def test_repository_get_user(test_repo):
    user = test_repo.get_user('m.a.r.johnson@me.com')
    assert user.user_id == 1


def test_repository_non_existent_user(test_repo):
    user = test_repo.get_user('fake@email.com')
    assert user is None


def test_add_movie_get_by_title(test_repo):
    movie = Movie(
        title='Harry Potter and the Order of the Phoenix',
        year=2007,
        id=1001
    )
    test_repo.add_movie(movie)
    assert test_repo.get_movie_by_title('Harry Potter and the Order of the Phoenix').title == movie.title


def test_add_movie_get_by_id(test_repo):
    movie = Movie(
        title='Made-Up Movie',
        year=1994,
        id=1001
    )
    test_repo.add_movie(movie)
    assert test_repo.get_movie_by_id(1001) is movie


def test_add_genre_get_genres(test_repo):
    test_genre = Genre(
        genre_type='TEST'
    )
    test_repo.add_genre(test_genre)
    genres = test_repo.get_genres()
    assert test_genre in genres


def test_get_movies_by_genre(test_repo):
    genres = test_repo.get_genres()
    movies = test_repo.get_movies_by_genre(genres[0])
    assert genres[0] in movies[0].genres


def test_get_movies_by_director(test_repo):
    movie = test_repo.get_movie_by_id(1)
    director = movie.director
    movies = test_repo.get_movies_by_director(director)
    assert director == movies[2].director


def test_get_movies_by_actor(test_repo):
    movie = test_repo.get_movie_by_id(5)
    actor = movie.actors[0]
    movies = test_repo.get_movies_by_actor(actor)
    assert actor in movies[5].actors


def test_get_movies_by_id(test_repo):
    movie = test_repo.get_movie_by_id(1)
    assert movie.title == 'Guardians of the Galaxy'


def test_get_movie_reviews(test_repo):
    movie = test_repo.get_movie_by_id(1)
    reviews = test_repo.get_movie_reviews(movie)
    assert len(reviews) is 2


def test_add_review(test_repo):
    user = test_repo.get_user_by_id(3)
    movie = test_repo.get_movie_by_id(7)
    review = Review(
        movie=movie,
        review_text='What a lovely film. I would recommend to others.',
        rating=7,
        user=user
    )
    test_repo.add_review(review)
    assert review in test_repo.get_movie_reviews(movie)


def test_get_movies(test_repo):
    movies = test_repo.get_movies()
    assert len(movies) == 1000


