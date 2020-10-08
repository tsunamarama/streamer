from flask import Blueprint, render_template, request

import streamer.utilities.utilities as utilities
import streamer.authentication.services as auth_services
import streamer.adapters.repository as repo


watchlist_bp = Blueprint('watchlist_bp', __name__)


@watchlist_bp.route('/watchlist', methods=['GET'])
def watchlist():
    user = auth_services.get_user(request.args.get('username'), repo.repo_instance)
    movies = user
    return render_template(
        'watchlist/watchlist.html',
        movies=utilities.get_selected_movies()
    )
