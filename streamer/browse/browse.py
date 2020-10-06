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


@browse_bp.route('/browse', methods=['GET'])
def browse():
    return render_template(
        'browse/browse.html',
        selected_movies=0
    )


@browse_bp.route('/browse_by_genre', methods=['GET'])
def browse_by_genre():
    return render_template(
        'browse/browse.html',
        selected_movies=0
    )


@browse_bp.route('/browse_by_actor', methods=['GET'])
def browse_by_actor():
    return render_template(
        'browse/browse.html',
        selected_movies=0
    )


@browse_bp.route('/browse_by_director', methods=['GET'])
def browse_by_director():
    return render_template(
        'browse/browse.html',
        selected_movies=0
    )


@browse_bp.route('/browse_by_rank', methods=['GET'])
def browse_by_rank():
    return render_template(
        'browse/browse.html',
        selected_movies=0
    )
