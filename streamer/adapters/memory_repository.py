from typing import List

import csv
import os

from streamer.adapters.repository import AbstractRepository
# from streamer.domain.actor import Actor
# from streamer.domain.director import Director
# from streamer.domain.genre import Genre
# from streamer.domain.movie import Movie
# from streamer.domain.review import Review
# from streamer.domain.user import User
from streamer.domain.model import Actor, Director, Genre, Movie, Review, User


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__users = set()
        self.__movies = set()
        self.__reviews = set()
        self.__actors = set()
        self.__directors = set()
        self.__genres = set()

    def add_user(self, user: User):
        self.__users.add(user)

    def get_user(self, user_name: str) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def get_user_by_id(self, uid: int) -> User:
        return next((user for user in self.__users if user.user_id == uid), None)

    def add_movie(self, movie: Movie):
        self.__movies.add(movie)

    def get_movie_by_id(self, movie_id: int) -> Movie:
        return next((movie for movie in self.__movies if movie.movie_id == movie_id), None)

    def get_movie_by_title(self, title: str) -> Movie:
        return next((movie for movie in self.__movies if movie.title.lower() == title.lower()), None)

    def get_movies(self) -> List[Movie]:
        return list(self.__movies)

    def get_movies_by_genre(self, genre: Genre) -> List[Movie]:
        return [movie for movie in self.__movies if genre in movie.genres]

    def get_movies_by_actor(self, actor: Actor) -> List[Movie]:
        return [movie for movie in self.__movies if actor in movie.actors]

    def get_movies_by_director(self, director: Director) -> List[Movie]:
        return [movie for movie in self.__movies if director == movie.director]

    def get_movies_by_id(self, id_list: list) -> List[Movie]:
        return [movie for movie in self.__movies if movie.movie_id in id_list]

    def add_review(self, review: Review):
        review.movie.reviews.append(review)
        review.user.reviews.append(review)
        super().add_review(review)
        self.__reviews.add(review)

    def get_movie_reviews(self, movie: Movie) -> List[Review]:
        return [review for review in self.__reviews if review.movie == movie]

    def add_director(self, director: Director):
        self.__directors.add(director)

    def add_actor(self, actor: Actor):
        self.__actors.add(actor)

    def add_genre(self, genre: Genre):
        self.__genres.add(genre)

    def get_genres(self) -> List[Genre]:
        return [genre for genre in self.__genres]


def read_datafile(filename: str):
    with open(filename, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        header_row = next(reader)
        for row in reader:
            row = [item.strip() for item in row]
            yield row


def load_movies(path: str, repo: MemoryRepository):
    for row in read_datafile(os.path.join(path, 'movies.csv')):
        movie = Movie(
            title=row[1],
            year=int(row[6]),
            desc=row[3],
            director=Director(row[4]),
            mins=int(row[7]),
            rank=int(row[0])
        )
        repo.add_movie(movie)
        repo.add_director(movie.director)
        for actor in row[5].split(','):
            new_actor = Actor(actor.strip())
            movie.add_actor(new_actor)
            repo.add_actor(new_actor)
        for genre in row[2].split(','):
            new_genre = Genre(genre.strip())
            movie.add_genre(new_genre)
            repo.add_genre(new_genre)


def load_users(path: str, repo: MemoryRepository):
    for row in read_datafile(os.path.join(path, 'users.csv')):
        user = User(
            user_name=row[1],
            password=row[2],
            first_name=row[3],
            last_name=row[4]
        )
        repo.add_user(user)


def load_reviews(path: str, repo: MemoryRepository):
    for row in read_datafile(os.path.join(path, 'reviews.csv')):
        review = Review(
            movie=repo.get_movie_by_title(row[0]),
            review_text=row[1],
            rating=int(row[2]),
            user=repo.get_user(row[4])
        )
        review.user.reviews.append(review)
        review.movie.reviews.append(review)
        repo.add_review(review)


def load_data(path: str, repo: MemoryRepository):
    load_users(path, repo)
    load_movies(path, repo)
    load_reviews(path, repo)
