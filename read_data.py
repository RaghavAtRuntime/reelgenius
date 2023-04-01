"""This Python module contains the functions used to read data from the datasets, and populate the given graph.

This file is Copyright (c) 2023 Rohan Bhalla, Raghav Sinha, Grant Bogner, and Bora Celebi.
"""
import csv

from graph import Graph
from movie_user_classes import Movie


def import_movies(movie_file: str, graph: Graph) -> None:
    """Reads the movie_file and populates graph._movies
    """
    with open(movie_file, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movie_id = int(row[0])
            title = row[1]
            movie = Movie(movie_id, title)
            graph.add_movie(movie)


def import_ratings(rating_file: str, graph: Graph) -> None:
    """Reads the ratings_file and creates new users, populates graph._users and modifies Movie.ratings and User.ratings
    Preconditions:
     - each entry in ratings_file is unique
    """
    with open(rating_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            curr_userid = int(row[0])
            movie_id = int(row[1])
            rating = float(row[2])
            curr_user = graph.find_or_add_user(curr_userid)  # Does our dict allocation for us
            graph.add_rating(curr_user, movie_id, rating)
