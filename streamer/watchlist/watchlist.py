from flask import Blueprint, render_template, request, session
from streamer.authentication.authentication import login_required

import streamer.watchlist.services as services
import streamer.adapters.repository as repo


watchlist_bp = Blueprint('watchlist_bp', __name__)


@watchlist_bp.route('/watchlist', methods=['GET'])
def watchlist():
    movies = services.get_watchlist(session['username'], repo.repo_instance)
    count = len(movies)
    return render_template(
        'watchlist/watchlist.html',
        movies=movies,
        count=count
    )


@watchlist_bp.route('/add_to_watchlist', methods=['GET'])
@login_required
def add_to_watchlist():
    movie_id = int(request.args.get('id'))
    services.add_to_watchlist(movie_id, session['username'], repo.repo_instance)
    return render_template(
        'watchlist/watchlist.html',
        movies=services.get_watchlist(session['username'], repo.repo_instance)
    )


@watchlist_bp.route('/remove_from_watchlist', methods=['GET'])
def remove_from_watchlist():
    movie_id = int(request.args.get('id'))
    services.remove_from_watchlist(movie_id, session['username'], repo.repo_instance)
    return render_template(
        'watchlist/watchlist.html',
        movies=services.get_watchlist(session['username'], repo.repo_instance)
    )
