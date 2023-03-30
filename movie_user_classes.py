# Movie and User Classes
from __future__ import annotations
import doctest
import python_ta


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
        A list of recommended movies sorted by their recommendation score

    Representation Invariants:
    - self.user_id > 0
    - all({1 <= self.movie_ratings[m] <= 5 for m in self.movie_ratings})
    """
    user_id: int
    movie_ratings: dict[int, float]
    user_compats: dict[int, float]
    recommendations: list[int]

    def __init__(self, user_id: int) -> None:
        """Initialize this user with the given user_id, and with empty movie_ratings,
        user_compats, and recommendations"""
        self.user_id = user_id
        self.movie_ratings = {}
        self.user_compats = {}
        self.recommendations = []

    def get_movies(self) -> set[int]:
        """Return a set of movie ids for movies this user has rated
        """
        return set(self.movie_ratings)

    def get_rating(self, movie_id: int) -> float:
        """ Return the score this user gave for the movie with id == movie_id

        Preconditions:
        - movie_id in self.movie_ratings
        """
        return self.movie_ratings[movie_id]


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
    user_ratings: dict[int, float]

    def __init__(self, movie_id: int, title: str) -> None:
        """Initialize the given movie with the given movie_id and title, and with empty user_ratings
        """
        self.movie_id = movie_id
        self.title = title
        self.user_ratings = {}

    def get_users(self) -> list[int]:
        """Return a set of user ids for users that have rated this movie
        """
        return list(self.user_ratings)


class Graph:
    """ A class to represent a graph

    Instance Attributes:
    - _movies:
        A mapping of the movies stored in this graph. Each key is a movie id and each value is a Movie object
    - _users:
        A mapping of the users stored in this graph. Each key is a user id and each value is a User object
    """
    _movies: dict[int, Movie]
    _users: dict[int, User]

    def __init__(self) -> None:
        self._movies = {}
        self._users = {}

    def get_all_users(self) -> list[User]:
        """ Returns all users in this graph
        """
        users_so_far = []
        for i in self._users:
            users_so_far.append(self._users[i])
        return users_so_far

    def add_movie(self, movie: Movie) -> None:
        """ Adds movie to self._movies. If movie.movie_id is already a key in self._movies, the object stored at that
        key is replaced by movie instead.
        """
        self._movies[movie.movie_id] = movie

    def add_user(self, user: User) -> None:
        """ Adds user to self._users
        """
        self._users[user.user_id] = user

    def get_movie(self, movie_id: int) -> Movie:
        """ Returns the movie in this graph with id == movie_id

        Preconditions:
        - movie_id in self._movies
        """
        return self._movies[movie_id]

    def get_user(self, user_id: int) -> User:
        """ Returns the user in this graph with id == user_id

        Preconditions:
        - user_id in self._users
        """
        return self._users[user_id]

    def user_exists(self, user_id: int) -> bool:
        """ Returns whether the user with id == user_id is in this graph
        """
        return user_id in self._users


if __name__ == '__main__':
    doctest.testmod()
    python_ta.check_all(config={
        'extra-imports': ['__future__', 'doctest'],
        'allowed-io': [],
        'max-line-length': 120
    })
