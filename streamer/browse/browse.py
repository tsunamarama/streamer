from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

import streamer.adapters.repository as repo
import streamer.utilities.utilities as utilities
import streamer.browse.services as services
import streamer.utilities.services as util_services


browse_bp = Blueprint('browse_bp', __name__)


@browse_bp.route('/browse', methods=['GET'])
def browse():
    return render_template(
        'browse/browse.html',
        movies=utilities.get_selected_movies(),
        subtitle='Search our database by genre, actor, director or movie',
        genre_labels=services.get_genre_labels(repo.repo_instance),
        actor_labels=services.get_actor_labels(repo.repo_instance),
        director_labels=services.get_director_labels(repo.repo_instance),
        movie_labels=services.get_movie_labels(repo.repo_instance)
    )


@browse_bp.route('/browse_by_genre', methods=['GET'])
def browse_by_genre():
    genre_id = int(request.args.get('id'))
    movies = services.get_genre_movies(genre_id, repo.repo_instance)
    for movie in movies:
        movie['url'] = url_for('movie_bp.movie_by_id', id=movie['id'])
    return render_template(
        'browse/browse.html',
        movies=movies,
        subtitle=services.get_genre_subtitle(genre_id, repo.repo_instance),
        genre_labels=services.get_genre_labels(repo.repo_instance),
        actor_labels=services.get_actor_labels(repo.repo_instance),
        director_labels=services.get_director_labels(repo.repo_instance),
        movie_labels=services.get_movie_labels(repo.repo_instance)
    )


@browse_bp.route('/browse_by_actor', methods=['GET'])
def browse_by_actor():
    actor_id = int(request.args.get('id'))
    movies = services.get_actor_movies(actor_id, repo.repo_instance)
    # for movie in movies:
    #     movie['url'] = url_for('movie_bp.movie_by_id', id=movie['id'])
    return render_template(
        'browse/browse.html',
        movies=movies,
        subtitle=services.get_actor_subtitle(actor_id, repo.repo_instance),
        genre_labels=services.get_genre_labels(repo.repo_instance),
        actor_labels=services.get_actor_labels(repo.repo_instance),
        director_labels=services.get_director_labels(repo.repo_instance),
        movie_labels=services.get_movie_labels(repo.repo_instance)
    )


@browse_bp.route('/browse_by_director', methods=['GET'])
def browse_by_director():
    director_id = int(request.args.get('id'))
    movies = services.get_director_movies(director_id, repo.repo_instance)
    # for movie in movies:
    #     movie['url'] = url_for('movie_bp.movie_by_id', id=movie['id'])
    return render_template(
        'browse/browse.html',
        movies=movies,
        subtitle=services.get_director_subtitle(director_id, repo.repo_instance),
        genre_labels=services.get_genre_labels(repo.repo_instance),
        actor_labels=services.get_actor_labels(repo.repo_instance),
        director_labels=services.get_director_labels(repo.repo_instance),
        movie_labels=services.get_movie_labels(repo.repo_instance)
    )


"""
@browse_bp.route('/browse_by_movie', methods=['GET'])
def browse_by_movie():
    movie_id = int(request.args.get('id'))
    movie = util_services.get_movie(movie_id, repo.repo_instance)
    movie['url'] = url_for('movie_bp.movie_by_id', id=movie['id'])
    return render_template(
        'browse/browse.html',
        movies=movie,
        subtitle=services.get_movie_subtitle(movie_id, repo.repo_instance),
        genre_labels=services.get_genre_labels(repo.repo_instance),
        actor_labels=services.get_actor_labels(repo.repo_instance),
        director_labels=services.get_director_labels(repo.repo_instance),
        movie_labels=services.get_movie_labels(repo.repo_instance)
    )"""
