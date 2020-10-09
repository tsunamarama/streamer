import pytest

from flask import session


def test_register(client):
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200
    response = client.post(
        '/authentication/register',
        data={'username': 'h.potter@hogwarts.co.uk', 'password': 'Wingardiumleviosa1'}
    )
    assert response.headers['Location'] == 'http://localhost/authentication/login'


@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Your username is required'),
        ('mj', '', b'Your username is too short'),
        ('test', '', b'Your password is required'),
        ('test', 'test', b'Your password must at least 8 characters, and contain an upper case letter, a lower case letter and a digit'),
        ('m.a.r.johnson@me.com', 'Test#6^0', b'Your username is already taken - please supply another'),
))
def test_register_with_invalid_input(client, username, password, message):
    response = client.post(
        '/authentication/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost:5000/'
    with client:
        client.get('/')
        assert session['username'] == 'dawn@aucklanduni.ac.nz'


def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session


def test_login_required_to_review(client):
    response = client.post('/submit_review')
    assert response.headers['Location'] == 'http://localhost/authentication/login'


def test_review(client, auth):
    auth.login()
    movie_id = None
    response = client.get('/submit_review?id=' + str(movie_id))
    response = client.post(
        '/comment',
        data={'id': movie_id, 'review_text': 'Who needs quarantine?', 'rating': 2, 'user': session['username']}
    )
    assert response.headers['Location'] == 'http://localhost/articles_by_date?date=2020-02-29&view_comments_for=2'
