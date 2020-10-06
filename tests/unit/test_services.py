import pytest

from streamer.authentication.services import AuthenticationException
from streamer.browse.services import NonExistentMovieException

from streamer.browse import services as browse_services
from streamer.authentication import services as auth_services


def test_add_user(test_repo):
    user_name = 'mjoh781@aucklanduni.ac.nz'
    password = 'selera'
    auth_services.add_user(user_name, password, 'Michael', 'Johnson', test_repo)
    user_dict = auth_services.get_user(user_name, test_repo)
    assert user_dict['username'] == user_name
    assert user_dict['password'].startswith('pbkdf2:sha256:')


def test_add_existing_user(test_repo):
    user_name = 'm.a.r.johnson@me.com'
    password = 'parisbutter'
    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(user_name, password, 'Michael', 'Johnson', test_repo)


def test_auth_valid_cred(test_repo):
    user_name = 'mjoh781@aucklanduni.ac.nz'
    password = 'selera'
    auth_services.add_user(user_name, password, 'Michael', 'Johnson', test_repo)
    try:
        auth_services.auth_user(user_name, password, test_repo)
    except AuthenticationException:
        assert False


def test_auth_invalid_cred(test_repo):
    user_name = 'mjoh781@aucklanduni.ac.nz'
    password = 'selera'
    auth_services.add_user(user_name, password, 'Michael', 'Johnson', test_repo)
    with pytest.raises(auth_services.AuthenticationException):
        auth_services.auth_user(user_name, 'fakepassword', test_repo)


def test_add_review(test_repo):
    review_text = 'This was a terrible film'
    browse_services.add_review(
        movie_id=test_repo.get_movie_by_title('Guardians of the Galaxy').movie_id,
        review_text=review_text,
        rating=2,
        user_name='m.a.r.johnson@me.com',
        repo=test_repo
    )
    reviews_as_dict = browse_services.get_reviews_for_movie(
        movie_id=test_repo.get_movie_by_title('Guardians of the Galaxy').movie_id,
        repo=test_repo)
    assert next(
        (dic['review_text'] for dic in reviews_as_dict if dic['review_text'] == review_text), None) is not None


def test_add_review_non_existent_movie(test_repo):
    with pytest.raises(NonExistentMovieException):
        browse_services.add_review(
            movie_id=11111111,
            review_text='This movie does not exist',
            rating=2,
            user_name='m.a.r.johnson@me.com',
            repo=test_repo
        )


def test_add_review_unknown_user(test_repo):
    with pytest.raises(browse_services.UnknownUserException):
        browse_services.add_review(
            movie_id=test_repo.get_movie_by_title('Guardians of the Galaxy').movie_id,
            review_text='This was a terrible film',
            rating=2,
            user_name='fake@email.com',
            repo=test_repo
        )


def test_get_movie_reviews(test_repo):
    movie = test_repo.get_movie_by_title('Guardians of the Galaxy')
    reviews_as_dict = browse_services.get_reviews_for_movie(movie.movie_id, test_repo)
    assert len(reviews_as_dict) == len(movie.reviews)
    movie_ids = set([review['movie'].movie_id for review in reviews_as_dict])
    assert movie.movie_id in movie_ids and len(movie_ids) == 1


def test_get_movie(test_repo):
    movie = test_repo.get_movie_by_title('Guardians of the Galaxy')
    movie_as_dict = browse_services.get_movie(
        movie_id=movie.movie_id,
        repo=test_repo
    )
    assert movie_as_dict['id'] == movie.movie_id
    assert movie_as_dict['title'] == movie.title
    assert movie_as_dict['year'] == movie.year
    assert movie_as_dict['desc'] == movie.description
    assert movie_as_dict['director'] == movie.director
    assert movie_as_dict['runtime'] == movie.runtime_minutes
    actors = [actor_dict['name'] for actor_dict in movie_as_dict['actors']]
    genres = [genre_dict['genre'] for genre_dict in movie_as_dict['genres']]
    reviews_movie = [review_dict['movie'] for review_dict in movie_as_dict['reviews']]
    reviews_review_text = [review_dict['review_text'] for review_dict in movie_as_dict['reviews']]
    reviews_rating = [review_dict['rating'] for review_dict in movie_as_dict['reviews']]
    reviews_timestamp = [review_dict['timestamp'] for review_dict in movie_as_dict['reviews']]
    reviews_user = [review_dict['user'] for review_dict in movie_as_dict['reviews']]
    assert movie.actors[0].actor_full_name in actors
    assert movie.genres[0].genre_type in genres
    assert movie.reviews[0].movie in reviews_movie
    assert movie.reviews[0].review_text in reviews_review_text
    assert movie.reviews[0].rating in reviews_rating
    assert movie.reviews[0].timestamp in reviews_timestamp
    assert movie.reviews[0].user.user_name in reviews_user


def test_get_reviews_non_existent_movie(test_repo):
    with pytest.raises(NonExistentMovieException):
        print(browse_services.get_reviews_for_movie(11111111, test_repo))


def test_get_reviews_movie_without_reviews(test_repo):
    reviews_as_dict = browse_services.get_reviews_for_movie(
        movie_id=test_repo.get_movie_by_title('Trolls').movie_id,
        repo=test_repo
    )
    assert len(reviews_as_dict) == 0


def test_get_movies_by_id(test_repo):
    movie_1 = test_repo.get_movie_by_title('Prometheus').movie_id
    movie_2 = test_repo.get_movie_by_title('Rogue One').movie_id
    movie_3 = test_repo.get_movie_by_title('Moana').movie_id
    movie_4 = 11111111
    target_ids = [movie_1, movie_2, movie_3, movie_4]
    movies_as_dict = browse_services.get_movies_by_id(target_ids, test_repo)
    assert len(movies_as_dict) == 3
    movie_ids = [movie['id'] for movie in movies_as_dict]
    assert {movie_1, movie_2, movie_3}.issubset(movie_ids)


def test_get_movies_by_genre(test_repo):
    genres = test_repo.get_genres()
    movies_as_dict = browse_services.get_movies_by_genre(genres[0], test_repo)
    movie_genres = [movie['genres'] for movie in movies_as_dict]
    assert any(movie['genre'] == genres[0].genre_type for movie in movie_genres[0])
