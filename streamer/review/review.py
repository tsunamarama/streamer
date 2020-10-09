from flask import Blueprint, render_template, request, redirect, session, url_for
from flask_wtf import FlaskForm
from streamer.authentication.authentication import login_required
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired

import streamer.utilities.utilities as utilities
import streamer.movie.services as services
import streamer.adapters.repository as repo


review_bp = Blueprint('review_bp', __name__)


@review_bp.route('/submit_review', methods=['GET', 'POST'])
@login_required
def submit_review():
    movie_id = int(request.args.get('id'))
    movie = utilities.get_selected_movie_by_id(movie_id)
    form = ReviewForm()
    if form.validate_on_submit():
        services.add_review(
            movie_id=movie_id,
            review_text=form.review_text.data,
            rating=int(form.rating.data),
            user_name=session['username'],
            repo=repo.repo_instance
        )
        return redirect(url_for('movie_bp.movie_by_id', id=movie_id))
    return render_template(
        'review/review.html',
        form=form,
        movie=movie
    )


class ReviewForm(FlaskForm):
    review_text = StringField('Review', [
        DataRequired(message='You must enter a review')])
    rating = DecimalField('Rating', [
        DataRequired(message='A rating is required')])
    submit = SubmitField('Submit')
