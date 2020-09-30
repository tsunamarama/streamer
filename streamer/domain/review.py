from datetime import datetime
from streamer.domain.movie import Movie
from streamer.domain.user import User


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int, user: User):
        self.__movie = movie
        self.__review_text = review_text.strip()
        if 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now()
        self.__user = user

    def __repr__(self):
        return f'<Review {self.__movie}, {self.__rating}>'

    def __eq__(self, other):
        return (self.__movie, self.__review_text, self.__rating, self.__timestamp) == \
               (other.__movie, other.__review_text, other.__rating, other.__timestamp)

    def __hash__(self):
        return hash(self.__movie)

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @review_text.setter
    def review_text(self, new_text: str):
        self.__review_text = new_text.strip()

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, new_rating: int):
        self.__rating = new_rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    @property
    def user(self) -> User:
        return self.__user
