from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import streamer.adapters.repository as repo
import streamer.utilities.utilities as utilities
import streamer.browse.services as services

from streamer.authentication.authentication import login_required


browse_bp = Blueprint('browse_bp', __name__)


@browse_bp.route('/movies_by_genre', methods=['GET'])
def movies_by_date():
    target_genre = request.args.get('genre')
    return render_template(
        'browse/movies.html',
        title='Movies',
        movies_title=target_genre
    )
