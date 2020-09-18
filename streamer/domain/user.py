from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, user_name: str, password: str):
        self.__user_name = user_name.lower().strip()
        self.__password = password
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = int()

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    @property
    def user_name(self) -> str:
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name: str):
        self.__user_name = user_name.lower().strip()

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, movies: list):
        self.__watched_movies = movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews: list):
        self.__reviews = reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, minutes: int):
        self.__time_spent_watching_movies_minutes = minutes

    def watch_movie(self, movie: Movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        if review not in self.__reviews:
            self.__reviews.append(review)


class TestUserMethods:
    def test_watch_movie(self):
        user = User('michael', 'pw123456')
        movie = Movie('Call Me By Your Name', 2017)
        movie.runtime_minutes = 127
        user.watch_movie(movie)
        assert user.time_spent_watching_movies_minutes == 127
        assert len(user.watched_movies) == 1
        user.add_review(Review(user.watched_movies[0], 'This was a great film', 9))
        user.watch_movie(movie)
        assert user.time_spent_watching_movies_minutes == 127 * 2
        assert len(user.watched_movies) == 1

    def test_hash(self):
        user1 = User('MJ', '12345678')
        user2 = User('BJ', '87654321')
        user3 = User('MJ', '12345678')
        assert hash(user1) != hash(user2)
        assert hash(user1) == hash(user3)
