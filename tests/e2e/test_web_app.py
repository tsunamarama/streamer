import pytest

from flask import session


def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session


def test_login_required_to_review(client):
    response = client.post('/submit_review')
    assert response.headers['Location'] == 'http://localhost/authentication/login'
