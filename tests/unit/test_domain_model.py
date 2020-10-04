import pytest

from streamer.domain.model import Actor, Director, Genre, Movie, Review, User, WatchList


@pytest.fixture()
def user_1():
    return User(
        user_name='mjoh781@aucklanduni.ac.nz',
        password='giraffe',
        first_name='Michael',
        last_name='Johnson'
    )


@pytest.fixture()
def user_2():
    return User(
        user_name='mjoh781@aucklanduni.ac.nz',
        password='giraffe',
        first_name='Michael',
        last_name='Johnson'
    )


@pytest.fixture()
def actor_1():
    return Actor(
        actor_full_name='Brad Pitt'
    )


@pytest.fixture()
def actor_2():
    return Actor(
        actor_full_name='Angelina Jolie'
    )


@pytest.fixture()
def director():
    return Director(
        director_full_name='Doug Liman'
    )


@pytest.fixture()
def genre_1():
    return Genre(
        genre_type='Comedy'
    )


@pytest.fixture()
def movie_1(director):
    return Movie(
        title='Mr. & Mrs. Smith',
        year=2005,
        desc='This is a description',
        director=director,
        mins=120
    )


@pytest.fixture()
def movie_2(director):
    return Movie(
        title='Mr. & Mrs. Smith',
        year=2006,
        desc='This is a description',
        director=director,
        mins=120
    )


@pytest.fixture()
def review_1(movie_1, user_1):
    return Review(
        movie=movie_1,
        review_text='',
        rating=7,
        user=user_1
    )


class TestActor:
    def test_add_actor_colleague_check_if_worked_with(self, actor_1, actor_2):
        actor_1.add_actor_colleague(actor_2)
        assert actor_1.check_if_this_actor_worked_with(actor_2) is True
        assert actor_2.check_if_this_actor_worked_with(actor_1) is True

    def test_check_repr(self, actor_2):
        assert repr(actor_2) == "<Actor Angelina Jolie>"

    def test_invalid_actor_name(self):
        empty_str_actor = Actor('')
        int_actor = Actor(42)
        assert int_actor.actor_full_name is None and empty_str_actor.actor_full_name is None


class TestDirector:
    def test_check_repr(self, director):
        assert repr(director) == '<Director Doug Liman>'

    def test_invalid_director_name(self):
        empty_str_director = Director('')
        int_director = Director(42)
        assert int_director.director_full_name is None and empty_str_director.director_full_name is None


class TestGenre:
    def test_chek_repr(self, genre_1):
        assert repr(genre_1) == '<Genre Comedy>'

    def test_invalid_genre_name(self):
        empty_str_genre = Genre("")
        int_genre = Genre(42)
        assert empty_str_genre.genre_type is None and int_genre.genre_type is None


class TestMovie:
    def test_runtime_minutes(self, movie_1):
        with pytest.raises(ValueError):
            movie_1.runtime_minutes = -1

    def test_add_actors(self, movie_1, actor_1, actor_2):
        movie_1.add_actor(actor_1)
        movie_1.add_actor(actor_2)
        assert repr(movie_1.actors) == '[<Actor Brad Pitt>, <Actor Angelina Jolie>]'
        assert len(movie_1.actors) == 2

    def test_remove_actors(self, movie_1, actor_1, actor_2):
        movie_1.add_actor(actor_1)
        movie_1.add_actor(actor_2)
        assert len(movie_1.actors) == 2
        movie_1.remove_actor(actor_1)
        assert len(movie_1.actors)

    def test_movie_hash(self, movie_1, movie_2):
        assert hash(movie_1) != hash(movie_2)
        movie_3 = Movie(
            title='Mr. & Mrs. Smith',
            year=2005,
            desc='',
            director=director,
            mins=120
        )
        assert hash(movie_1) == hash(movie_3)

    def test_add_remove_genre(self, movie_1, genre_1):
        movie_1.add_genre(genre_1)
        assert len(movie_1.genres) == 1
        assert repr(movie_1.genres) == '[<Genre Comedy>]'
        movie_1.remove_genre(genre_1)
        assert len(movie_1.genres) == 0

    def test_movie_year(self, movie_1):
        movie_1.year = 1899
        assert movie_1.year == 2005
        movie_2 = Movie('Mr. & Mrs. Smith', 1899)
        assert movie_2.year is None

    def test_movie_description(self, movie_1):
        movie_1.description = 123
        assert movie_1.description == 'This is a description'


class TestReview:
    def test_review_rating(self, review_1):
        pass


class TestUser:
    def test_user_hash(self, user_1, user_2):
        assert hash(user_1) == hash(user_2)
        user_2.user_name = 'fake@email.com'
        assert hash(user_1) != hash(user_2)

    def test_watch_movie(self, user_1, movie_1):
        assert len(user_1.watched_movies) == 0
        user_1.watch_movie(movie_1)
        assert len(user_1.watched_movies) == 1
        assert user_1.time_spent_watching_movies_minutes == 120

    def test_add_review(self, user_1, movie_2):
        assert len(user_1.reviews) == 0
        review = Review(
            movie=movie_2,
            review_text='',
            rating=6,
            user=user_1
        )
        user_1.add_review(review)
        assert len(user_1.reviews) == 1
        assert user_1.reviews[0].rating == 6


class TestWatchList:
    def test_watchlist_size(self, user_1, movie_1):
        size = user_1.watchlist.size()
        assert size == 0

    def test_add_remove_to_watchlist_and_first_movie(self, user_1, movie_1, movie_2):
        watchlist = user_1.watchlist
        first_movie = watchlist.first_movie_in_watchlist()
        assert first_movie is None
        watchlist.add_movie(movie_1)
        first_movie = watchlist.first_movie_in_watchlist()
        assert first_movie == movie_1
        watchlist.add_movie(movie_2)
        assert watchlist.size() == 2
        watchlist.remove_movie(movie_2)
        assert watchlist.size() == 1
