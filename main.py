# Main File

import numpy as np
from movie_user_classes import User
from movie_user_classes import Movie
import csv

user_graph = {}
movie_dict = {}
movies_file = "data/movies.csv"
ratings_file = "data/ratings.csv"


def import_movies(movie_file: str, movies: dict) -> None:
    """Reads the movie_file and populates movies
    """
    with open(movie_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movie_id = int(row[0])
            title = row[1]
            movie = Movie(movie_id, title)
            movies[movie_id] = movie


def import_ratings(rating_file: str, users: dict) -> None:
    """Reads the ratings_file and populates users
    Preconditions:
     - each entry in ratings_file is unique
    """
    with open(rating_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            curr_userid = int(row[0])
            movie_id = int(row[1])
            rating = int(float(row[2]))
            curr_user = find_or_add_user(users, curr_userid)  # Does our dict allocation for us
            add_rating(curr_user, movie_id, rating)


def process_compat_users(users: dict[int, User]) -> None:
    """Finds compatible users for each user in users, and then updates their user_compats attribute accordingly
    """
    # for each user in userGraph
    #     compatUserIds = getMovieUsers(user.getMovies())
    # // add List as keys to Dict(might need conversion / typecast)
    # userCompats.add(compatUserIds)
    # TODO


def process_compat_score(users: dict[int, User]) -> None:
    """Compute each user in users compatability scores
    """
    # TODO
    # Idea: take the average of the differences in score between a user and its compat users


def process_movie_recommends(users: dict[int, User], n: int) -> None:
    """Generates a list of n movie reccommendations for each user in users and updates their recommended attribute
    accordingly
    """
    # TODO


def find_or_add_user(users: dict[int, User], id: int) -> User:
    """Returns the user in users with user_id == id. If such a user does not exist in users, the function instead
     creates a new user with user_id = id, adds it to users, and returns that user
    """
    # //same user
    # if(user != null & user.id == userId)
    #   return user
    # user = userGraph.find(userId)

    # //new user
    # if user = null
    #   user = new User(userId)
    #   userGraph.add(user)
    #   return user
    if id in users:
        return users[id]
    else:
        users[id] = User(id)
        return users[id]


def add_rating(user: User, movieid: int, rating: int) -> None:
    """Adds a rating with movie id and rating to the user's movie_ratings attribute
    and adds a user and its user rating to the movie's user_ratings attribute
    """
    user.movie_ratings[movieid] = rating
    movie = movie_dict[movieid]
    movie.user_ratings[user] = rating


def get_movie_users(movies: list[Movie]) -> set[int]:
    """Returns a set of ids for users who have a rating for at least one movie in movies
    """
    userSet = set()
    for movie in movies:
        userSet.add(movie.getUsers())
    # return userSet
    all_users = []
    for movie in movies:
        all_users.extend(movie.get_users())
    user_id_lst = [user.user_id for user in all_users]
    return set(user_id_lst)


if __name__ == '__main__':
    import_movies(movies_file, movie_dict)
    import_ratings(ratings_file, user_graph)
    process_compat_users(user_graph)
    # process_movie_recommends()
