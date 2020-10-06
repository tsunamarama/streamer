from flask import Blueprint
from flask import request, render_template
import streamer.utilities.utilities as utilities
import streamer.movie.services as services


movie_bp = Blueprint('movie_bp', __name__)


@movie_bp.route('/movie_by_id', methods=['GET'])
def movie_by_id():
    movie = utilities.get_selected_movie_by_id(int(request.args.get('id')))
    reviews = utilities.get_selected_movie_reviews_by_id(int(request.args.get('id')))
    return render_template(
        'movie/movie.html',
        movie=movie,
        reviews=reviews
    )


@movie_bp.route('/movie_by_title', methods=['GET'])
def movie_by_title():
    movie = utilities.get_selected_movie_by_title(request.args.get('title'))
    reviews = utilities.get_selected_movie_reviews_by_title(request.args.get('title'))
    return render_template(
        'movie/movie.html',
        movie=movie,
        reviews=reviews
    )