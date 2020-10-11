import pytest

from streamer.authentication.services import AuthenticationException
from streamer.utilities.services import NonExistentMovieException
from streamer.browse import services as browse_services
from streamer.authentication import services as auth_services
from streamer.movie import services as movie_services
from streamer.utilities import services as util_services


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
    movie_services.add_review(
        movie_id=test_repo.get_movie_by_title('Guardians of the Galaxy').movie_id,
        review_text=review_text,
        rating=2,
        user_name='m.a.r.johnson@me.com',
        repo=test_repo
    )
    reviews_as_dict = movie_services.get_movie_reviews(
        movie_id=test_repo.get_movie_by_title('Guardians of the Galaxy').movie_id,
        repo=test_repo
    )
    assert next(
        (dic['review_text'] for dic in reviews_as_dict if dic['review_text'] == review_text), None) is not None


def test_add_review_unknown_user(test_repo):
    with pytest.raises(movie_services.UnknownUserException):
        movie_services.add_review(
            movie_id=test_repo.get_movie_by_title('Guardians of the Galaxy').movie_id,
            review_text='This was a terrible film',
            rating=2,
            user_name='fake@email.com',
            repo=test_repo
        )


def test_get_reviews_movie_without_reviews(test_repo):
    reviews_as_dict = movie_services.get_movie_reviews(
        movie_id=test_repo.get_movie_by_title('Trolls').movie_id,
        repo=test_repo
    )
    assert len(reviews_as_dict) == 0
