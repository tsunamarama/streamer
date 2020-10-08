import pytest

# from streamer.adapters.repository import AbstractRepository
# from streamer.domain.actor import Actor
# from streamer.domain.director import Director
# from streamer.domain.genre import Genre
# from streamer.domain.movie import Movie
# from streamer.domain.review import Review
# from streamer.domain.user import User
from streamer.domain.model import Genre, Movie, Review, User

from streamer.adapters.repository import RepositoryException


def test_repository_add_user(test_repo):
    user = User(
        user_name='mjoh781@aucklanduni.ac.nz',
        password='cassia',
        first_name='Michael',
        last_name='Johnson'
    )
    test_repo.add_user(user)
    assert test_repo.get_user('mjoh781@aucklanduni.ac.nz') is user


def test_repository_get_user_by_id(test_repo):
    user = test_repo.get_user('h.valentine@adhb.govt.nz')
    assert user is test_repo.get_user_by_id(user.user_id)


def test_repository_get_user(test_repo):
    user = test_repo.get_user('m.a.r.johnson@me.com')
    assert user.password == 'parisbutter'


def test_repository_non_existent_user(test_repo):
    user = test_repo.get_user('fake@email.com')
    assert user is None


def test_add_movie_get_by_title(test_repo):
    movie = Movie(
        title='Harry Potter and the Order of the Phoenix',
        year=2007
    )
    test_repo.add_movie(movie)
    assert test_repo.get_movie_by_title('Harry Potter and the Order of the Phoenix').title == movie.title


def test_add_movie_get_by_id(test_repo):
    movie = Movie(
        title='Made-Up Movie',
        year=1994
    )
    test_repo.add_movie(movie)
    assert test_repo.get_movie_by_id(movie.movie_id) is movie


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
    movie = test_repo.get_movie_by_title('Guardians of the Galaxy')
    director = movie.director
    movies = test_repo.get_movies_by_director(director)
    assert director == movies[0].director


def test_get_movies_by_actor(test_repo):
    movie = test_repo.get_movie_by_title('Rogue One')
    actor = movie.actors[0]
    movies = test_repo.get_movies_by_actor(actor)
    assert actor in movies[0].actors


def test_get_movies_by_id(test_repo):
    movie = test_repo.get_movie_by_title('Guardians of the Galaxy')
    movie_id = movie.movie_id
    movie = test_repo.get_movie_by_id(movie_id)
    assert movie.title == 'Guardians of the Galaxy'


def test_get_movies_by_rank(test_repo):
    rank_list = [1, 2, 3]
    movies = test_repo.get_movies_by_rank(rank_list)
    movies.sort()
    assert movies[0].title == 'Guardians of the Galaxy'


def test_get_movie_reviews(test_repo):
    movie = test_repo.get_movie_by_title('Guardians of the Galaxy')
    reviews = test_repo.get_movie_reviews(movie)
    assert len(reviews) is 2


def test_add_review(test_repo):
    user = test_repo.get_user('c.arthars@bne.com.au')
    movie = test_repo.get_movie_by_title('Lion')
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
    assert len(movies) == 25


def test_get_movie_by_id(test_repo):
    movie_id = test_repo.get_movie_by_title('Guardians of the Galaxy').movie_id
    assert test_repo.get_movie_by_id(movie_id).title == 'Guardians of the Galaxy'


def test_get_genre_movie_list_len(test_repo):
    genres = test_repo.get_genres()
    genre = genres[0]
    print(genre)
    print(len(genre.movies))
