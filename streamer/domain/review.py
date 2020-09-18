from datetime import datetime
from domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        self.__movie = movie
        self.__review_text = review_text.strip()
        if 1 <= rating <= 10:
            self.__rating = rating
        else:
            self.__rating = None
        self.__timestamp = datetime.now()

    def __repr__(self):
        return f'<Review {self.__movie}, {self.__rating}>'

    def __eq__(self, other):
        return (self.__movie, self.__review_text, self.__rating, self.__timestamp) == (other.__movie, other.__review_text, other.__rating, other.__timestamp)

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp


class TestReviewMethods:
    def test_init(self):
        review = Review(Movie('Call Me By Your Name', 2017), 'This was an excellent film', 9)
        print(review.movie)
        print(review.review_text)
        print(review.rating)
        print(review.timestamp)
        print(review)