from flask import Blueprint, render_template, request, url_for

import streamer.utilities.utilities as utilities


movie_bp = Blueprint('movie_bp', __name__)


@movie_bp.route('/movie_by_id', methods=['GET'])
def movie_by_id():
    movie_id = int(request.args.get('id'))
    movie = utilities.get_selected_movie_by_id(movie_id)
    reviews = utilities.get_selected_movie_reviews_by_id(movie_id)
    submit_review_url = url_for('review_bp.submit_review', id=movie_id)
    add_to_watchlist_url = url_for('watchlist_bp.add_to_watchlist', id=movie_id)
    return render_template(
        'movie/movie.html',
        movie=movie,
        reviews=reviews,
        submit_review_url=submit_review_url,
        add_to_watchlist_url=add_to_watchlist_url
    )


@movie_bp.route('/movie_by_title', methods=['GET'])
def movie_by_title():
    movie = utilities.get_selected_movie_by_title(request.args.get('title'))
    reviews = utilities.get_selected_movie_reviews_by_title(request.args.get('title'))
    submit_review_url = url_for('review_bp.submit_review', id=movie['id'])
    add_to_watchlist_url = url_for('watchlist_bp.add_to_watchlist', id=movie['id'])
    return render_template(
        'movie/movie.html',
        movie=movie,
        reviews=reviews,
        submit_review_url=submit_review_url,
        add_to_watchlist_url=add_to_watchlist_url
    )
