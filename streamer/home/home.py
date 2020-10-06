from flask import Blueprint, render_template, url_for

import streamer.utilities.utilities as utilities


home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        selected_movies=utilities.get_selected_movies()
    )
