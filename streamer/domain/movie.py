import pytest
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


# USE CODE RUNNER VERSION

class Movie:
    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if type(year) is int and year >= 1900:
            self.__year = year
        else:
            self.__year = None
        self.__description = None
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if type(other) is Movie:
            return (self.__title, self.__year) == (other.__title, other.__year)

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
        else:
            self.__title = None

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year):
        if type(year) is int and year >= 1900:
            self.__year = year
        else:
            self.__title = None

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if description is not "" and type(description) is str:
            self.__description = description.strip()
        else:
            self.__title = None

    @property
    def director(self) -> str:
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
        if minutes <= 0:
            raise ValueError
        else:
            self.__runtime_minutes = minutes

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


class TestMovieMethods:
    def test_init(self):
        movie = Movie("Moana", 2016)
        assert repr(movie) == "<Movie Moana, 2016>"
        director = Director("Ron Clements")
        movie.director = director
        assert repr(movie.director) == "<Director Ron Clements>"
        movie.runtime_minutes = 107
        assert repr(movie.runtime_minutes) == "107"
        movie1 = Movie("Call Me By Your Name", 1899)
        assert movie1.year is None

    def test_runtime_minutes(self):
        movie = Movie("Call Me By Your Name", 2017)
        with pytest.raises(ValueError):
            movie.runtime_minutes = 0

    def test_hash(self):
        m1 = Movie("Call Me By Your Name", 2017)
        m2 = Movie("Call Me By Your Name", 2017)
        m3 = Movie("Call Me By Your Name", 2018)
        assert hash(m1) == hash(m2)
        assert hash(m1) != hash(m3)

    def test_actors(self):
        movie = Movie("Moana", 2016)
        actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
        for actor in actors:
            movie.add_actor(actor)
        assert repr(
            movie.actors) == "[<Actor Auli'i Cravalho>, <Actor Dwayne Johnson>, <Actor Rachel House>, <Actor Temuera Morrison>]"

    def test_rm_actor(self):  # these need to be fixed!!
        movie = Movie("Call Me By Your Name", 2017)
        actors = [Actor("Timothee Chalamet"), Actor("Armie Hammer")]
        movie.actors = actors
        assert repr(movie.actors) == "[<Actor Timothee Chalamet>, <Actor Armie Hammer>]"
        movie.remove_actor(Actor("Michael Stuhlberg"))
        assert repr(movie.actors) == "[<Actor Timothee Chalamet>, <Actor Armie Hammer>]"
        movie.remove_actor("Timothee Chalamet")
        assert repr(movie.actors) == "[<Actor Timothee Chalamet>, <Actor Armie Hammer>]"

    def test_lt(self):
        # check title
        movie = Movie("All Me By Your Name", 2017)
        movie1 = Movie("Call Me By Your Name", 2017)
        assert movie < movie1
        # check year
        movie2 = Movie("Call Me By Your Name", 2016)
        movie3 = Movie("Call Me By Your Name", 2017)
        assert movie2 < movie3
        # check both
        movie4 = Movie("Call Me By Your Name", 2015)
        movie5 = Movie("All Me By Your Name", 2017)
        assert movie4 < movie5

    def test_eq(self):
        movie = Movie("Call Me By Your Name", 2017)
        movie1 = Movie("Call Me By Your Name", 2017)
        assert movie == movie1

    def test_rndm(self):
        assert 1 < 2
