# Movie and User Classes
from __future__ import annotations


class User:
    """ A class that represents a user

    Instance Attributes
    - user_id:
        The id (unique identifier) for this user.
    - movie_ratings:
        A mapping containing the movies this user has rated. Each key is a movie id and each value is the
        score the user gave.
    - user_compats:
        A mapping containing compatible users. Each key is a user id, and each value is the compatibility score for the
        user
    - recommendations:
        A list of recommended movies for the user

    Representation Invariants:
    - self.user_id > 0
    - all({1 <= self.movie_ratings[m] <= 5 for m in self.movie_ratings})
    """
    user_id: int
    movie_ratings: dict[int, int]
    user_compats: dict[int, float]
    recommendations: list[Movie]

    def __init__(self, user_id: int):
        """Initialize this user with the given user_id, and with empty movie_ratings,
        user_compats, and recommendations"""
        self.user_id = user_id
        self.movie_ratings = {}
        self.user_compats = {}
        self.recommendations = []

    def get_movies(self) -> list[Movie]:
        """Return a list of movies this user has rated
        """



class Movie:
    """ A class that represents a movie

    Instance Attributes:
    - movie_id:
        The id (unique identifier) for this movie
    - title:
        The title of this movie
    - user_ratings:
        A mapping containing the users who have rated this movie. Each key is a user id and each value is the score
        given by the user

    Representation Invariants
    - self.movie_id > 0
    - all({1 <= self.user_ratings[u] <= 5 for u in self.user_ratings})
    """
    movie_id: int
    title: str
    user_ratings: dict[int, int]

    def __init__(self, movie_id: int, title: str):
        """Initialize the given movie with the given movie_id and title, and with empty user_ratings
        """

    def get_users(self, dict_users : dict[int, User]) -> list[User]:
        """Return a list of users that have rated this movie
        """
