from datetime import datetime


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if type(other) is Actor:
            return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):
        if type(other) is Actor:
            return self.__actor_full_name.lower() < other.__actor_full_name.lower()

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if colleague not in self.__colleagues:
            self.__colleagues.append(colleague)
        if self not in colleague.__colleagues:
            colleague.__colleagues.append(self)

    def check_if_this_actor_worked_with(self, colleague):
        return True if colleague in self.__colleagues else False


class Director:
    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if type(other) is Director:
            return self.__director_full_name == other.__director_full_name

    def __lt__(self, other):
        if type(other) is Director:
            return self.__director_full_name.lower() < other.__director_full_name.lower()

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:
    def __init__(self, genre_type: str):
        if genre_type == "" or type(genre_type) is not str:
            self.__genre_type = None
        else:
            self.__genre_type = genre_type.strip()

    @property
    def genre_type(self) -> str:
        return self.__genre_type

    def __repr__(self):
        return f"<Genre {self.__genre_type}>"

    def __eq__(self, other):
        if type(other) is Genre:
            return self.__genre_type == other.__genre_type

    def __lt__(self, other):
        if type(other) is Genre:
            return self.__genre_type.lower() < other.__genre_type.lower()

    def __hash__(self):
        return hash(self.__genre_type)


class Movie:
    def __init__(self, title: str, year: int, desc=None, director=None, mins=None, rank=int()):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if type(year) is int and year >= 1900:
            self.__year = year
        else:
            self.__year = None
        self.__description = desc
        self.__director = director
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = mins
        self.__reviews = []
        self.__rank = rank
        self.__movie_id = id(self)

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if type(other) is Movie:
            return self.__title == other.__title and self.__year == other.__year

    def __lt__(self, other):
        if type(other) is Movie:
            return (self.__title.lower(), self.__year) < (other.__title.lower(), other.__year)

    def __hash__(self):
        return hash((self.__title, self.__year))

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title):
        if title is not "" and type(title) is str:
            self.__title = title.strip()

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year):
        if type(year) is int and year >= 1900:
            self.__year = year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if description is not "" and type(description) is str:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, actors: list):
        self.__actors = actors

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, genres: list):
        self.__genres = genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, minutes: int):
        if minutes > 0:
            self.__runtime_minutes = minutes
        else:
            raise ValueError

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def rank(self) -> int:
        return self.__rank

    @property
    def movie_id(self) -> int:
        return self.__movie_id

    def add_actor(self, actor: Actor):
        if type(actor) is Actor and actor not in self.__actors:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if type(actor) is Actor and actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        if type(genre) is Genre and genre not in self.__genres:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if type(genre) is Genre and genre in self.__genres:
            self.__genres.remove(genre)

    def add_review(self, review):
        self.reviews.append(review)


class WatchList:
    def __init__(self):
        self.__watchlist = []

    @property
    def watchlist(self) -> list:
        return self.__watchlist

    def add_movie(self, movie: Movie):
        if movie not in self.__watchlist:
            self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watchlist:
            self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        if -len(self.__watchlist) <= index < len(self.__watchlist):
            return None
        else:
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) == 0:
            return None
        else:
            return self.__watchlist[0]


class User:
    def __init__(self, user_name: str, password: str, first_name: str, last_name: str):
        self.__user_id = id(self)
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
        user.add_review(self)
        movie.add_review(self)

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
