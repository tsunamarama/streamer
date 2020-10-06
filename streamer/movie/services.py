# from streamer.adapters.repository import AbstractRepository
# from streamer.domain.model import Actor, Genre, Movie, Review
# from typing import List
#
#
# def get_movie_reviews(movie_id: int, repo: AbstractRepository):
#     movie = repo.get_movie_by_id(movie_id)
#     reviews = repo.get_movie_reviews(movie)
#     return reviews_to_dict(reviews)
#
#
# def review_to_dict(review: Review):
#     return {
#         'review_text': review.review_text,
#         'rating': review.rating,
#         'timestamp': review.timestamp,
#         'user': review.user
#     }
#
#
# def reviews_to_dict(reviews: List[Review]):
#     return [review_to_dict(review) for review in reviews]