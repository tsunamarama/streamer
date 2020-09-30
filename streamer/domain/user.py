from streamer.domain.movie import Movie
from streamer.domain.watchlist import WatchList


class User:
    def __init__(self, user_name: str, password: str, first_name: str, last_name: str, user_id=int()):
        self.__user_id = user_id
        self.__user_name = user_name.lower().strip()
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = int()
        self.__watchlist = WatchList()

    def __repr__(self):
        return f'<User {self.__user_name}>'

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    @property
    def user_id(self):
        return self.__user_id

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

    @property
    def watchlist(self) -> WatchList:
        return self.__watchlist

    def watch_movie(self, movie: Movie):
        if movie not in self.__watched_movies:
            self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.__reviews:
            self.__reviews.append(review)
