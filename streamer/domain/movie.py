from streamer.domain.actor import Actor
from streamer.domain.director import Director
from streamer.domain.genre import Genre


class Movie:
    def __init__(self, title: str, year: int, desc=None, director=None, mins=None, id=int()):
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
        self.__id = id

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
    def id(self) -> int:
        return self.__id

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
