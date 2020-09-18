import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:
    def __init__(self, file_name: str):
        if type(file_name) is str:
            self.__file_name = file_name
            self.__dataset_of_movies = set()
            self.__dataset_of_actors = set()
            self.__dataset_of_directors = set()
            self.__dataset_of_genres = set()

    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        if type(file_name) is str:
            self.__file_name = file_name
        else:
            raise ValueError

    @property
    def dataset_of_movies(self) -> set:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> set:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> set:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            for row in movie_file_reader:
                movie = Movie(row['Title'], int(row['Year']))
                self.__dataset_of_movies.add(movie)
                movie.description = row['Description']
                movie.runtime_minutes = int(row['Runtime (Minutes)'])
                for actor in row['Actors'].split(','):
                    new_actor = Actor(actor.strip())
                    if new_actor not in self.__dataset_of_actors:
                        movie.add_actor(new_actor)
                        self.__dataset_of_actors.add(new_actor)
                    else:
                        for existing_actor in self.__dataset_of_actors:
                            if existing_actor == new_actor:
                                movie.add_actor(existing_actor)
                for genre in row['Genre'].split(','):
                    new_genre = Genre(genre.strip())
                    if new_genre not in self.__dataset_of_genres:
                        movie.add_genre(new_genre)
                        self.__dataset_of_genres.add(new_genre)
                    else:
                        for existing_genre in self.__dataset_of_genres:
                            if existing_genre == new_genre:
                                movie.add_genre(existing_genre)
                new_director = Director(row['Director'])
                if new_director not in self.__dataset_of_directors:
                    movie.director = new_director
                    self.__dataset_of_directors.add(new_director)
                else:
                    for existing_director in self.__dataset_of_directors:
                        if existing_director == new_director:
                            movie.director = existing_director


class TestReaderMethods:
    def test_init(self):
        data = MovieFileCSVReader('datafiles/Data1000Movies.csv')
        data.read_csv_file()
        assert len(data.dataset_of_movies) == 1000
        assert len(data.dataset_of_actors) == 1985
        assert len(data.dataset_of_directors) == 644
        assert len(data.dataset_of_genres) == 20

    def test_file(self):
        data = MovieFileCSVReader('datafiles/Data1000Movies.csv')
        data.read_csv_file()
