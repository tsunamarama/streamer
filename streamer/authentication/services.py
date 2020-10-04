from werkzeug.security import generate_password_hash, check_password_hash

from streamer.adapters.repository import AbstractRepository
# from streamer.domain.user import User
from streamer.domain.model import User


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class AuthenticationException(Exception):
    pass


def add_user(user_name: str, password: str, first_name: str, last_name: str, repo: AbstractRepository):
    if repo.get_user(user_name) is not None:
        raise NameNotUniqueException
    user_id = 0
    password_hash = generate_password_hash(password)
    repo.add_user(User(user_name, password_hash, first_name, last_name))


def get_user(user_name: str, repo: AbstractRepository):
    user = repo.get_user(user_name)
    if user is None:
        raise UnknownUserException
    return user_to_dict(user)


def user_to_dict(user: User):
    return {
        'username': user.user_name,
        'password': user.password
    }


def auth_user(user_name: str, password: str, repo: AbstractRepository):
    auth = False
    user = repo.get_user(user_name)
    if user is not None:
        auth = check_password_hash(user.password, password)
    if not auth:
        raise AuthenticationException