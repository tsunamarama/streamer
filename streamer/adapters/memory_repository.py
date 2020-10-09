from typing import List
from werkzeug.security import generate_password_hash

import csv
import os

from streamer.adapters.repository import AbstractRepository
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

    def get_movies_by_rank(self, rank_list: list) -> List[Movie]:
        return [movie for movie in self.__movies if movie.rank in rank_list]

    def get_genre_by_id(self, genre_id: int) -> Genre:
        return next((genre for genre in self.__genres if genre.genre_id == genre_id), None)

    def get_director_by_id(self, director_id: int) -> Genre:
        return next((director for director in self.__directors if director.director_id == director_id), None)

    def get_actor_by_id(self, actor_id: int) -> Genre:
        return next((actor for actor in self.__actors if actor.actor_id == actor_id), None)

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

    def get_actors(self) -> List[Actor]:
        return [actor for actor in self.__actors]

    def get_directors(self) -> List[Director]:
        return [director for director in self.__directors]


def read_datafile(filename: str):
    with open(filename, encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        header_row = next(reader)
        for row in reader:
            row = [item.strip() for item in row]
            yield row


def load_movies(path: str, repo: MemoryRepository):
    for row in read_datafile(os.path.join(path, 'movies.csv')):
        new_director = Director(row[4].strip())
        movie = Movie(
            title=row[1],
            year=int(row[6]),
            desc=row[3],
            director=new_director,
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
        password_hash = generate_password_hash(row[2])
        user = User(
            user_name=row[1],
            password=password_hash,
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
        repo.add_review(review)


def set_links(repo: MemoryRepository):
    movies = repo.get_movies()
    for movie in movies:
        genres = movie.genres
        actors = movie.actors
        director = movie.director
        for genre in genres:
            if movie.movie_id not in genre.movies:
                genre.add_movie(movie.movie_id)
        for actor in actors:
            if movie.movie_id not in actor.movies:
                actor.add_movie(movie.movie_id)
        if movie.movie_id not in director.movies:
            director.add_movie(movie.movie_id)


def load_data(path: str, repo: MemoryRepository):
    load_users(path, repo)
    load_movies(path, repo)
    load_reviews(path, repo)
    set_links(repo)
