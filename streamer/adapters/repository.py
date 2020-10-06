import abc
from typing import List
from streamer.domain.model import Actor, Director, Genre, Movie, Review, User

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        """"
        Adds a User to the repository.

        :param user: User
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username: str) -> User:
        """
        Returns the User for the given username from the repository.

        If there is no User with the given username, this method returns None.

        :param username: str
        :return: User
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        """
        Returns the User for the given user id username from the repository.

        If there is no User with the given user id, this method returns None.

        :param user_id: int
        :return: User
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """
        Adds a Movie to the repository.

        :param movie: Movie
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_id(self, movie_id: int) -> Movie:
        """
        Returns a Movie with the given movie_id from the repository.

        If there is no Movie with the given movie_id, this method returns None.

        :param movie_id: int
        :return Movie
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_by_title(self, title: str) -> Movie:
        """
        Returns a Movie for the given title from the repository.

        If there is no Movie with the given title, this method returns None.

        :param title: str
        :return: Movie
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies(self) -> List[Movie]:
        """
        Returns a list of Movies from the repository.

        :return: List[Movie]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_genre(self, genre: Genre) -> List[Movie]:
        """
        Returns a list of Movies that are of the target genre.

        If there are no Movies for the given genre, this method returns an empty list.

        :param genre: Genre
        :return: List[Movie]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_actor(self, actor: Actor) -> List[Movie]:
        """
        Returns a list of Movies that feature the target actor.

        If there are no Movies for the given actor, this method returns an empty list.

        :param actor: Actor
        :return: List[Movie]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_director(self, director: Director) -> List[Movie]:
        """
        Returns a list of Movies that are from the target director.

        If there are no Movies from the given director, this method returns an empty list.

        :param director: Director
        :return: List[Movie]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_id(self, id_list: list) -> List[Movie]:
        """
        Returns a list of Movies, whose ids match those in id_list, from the repository.

        If there are no matches, this method returns an empty list.

        :param id_list: list
        :return: List[Movie]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_rank(self, rank_list: list) -> List[Movie]:
        """
        Returns a list of Movies, whose ranks match those in rank_list, from the repository.

        If there are no matches, this method returns an empty list.

        :param rank_list:
        :return: List[Movie]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """
        Adds a Review to the repository.

        If the Review doesn't have bidirectional links with a Movie and a User, this method raises a
        RepositoryException and doesn't update the repository.

        :param review: Review
        """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Review not correctly attached to a User')
        if review.movie is None or review not in review.movie.reviews:
            raise RepositoryException('Review not correctly attached to a Movie')

    @abc.abstractmethod
    def get_movie_reviews(self, movie: Movie) -> List[Review]:
        """
        Returns a list of Reviews stored in the repository for a given Movie.

        :param movie: Movie
        :return: List[Review]
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        """
        Adds a Director to the repository.

        :param director: Director
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        """
        Adds an Actor to the repository.

        :param actor: Actor
        """
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        """
        Adds a Genre to the repository.

        :param genre: Genre
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        """
        Returns a list containing all Genres in the repository.

        :return: List[Genre]
        """
        raise NotImplementedError
