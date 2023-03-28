# Main File

import numpy as np
from movie_user_classes import User
from movie_user_classes import Movie
from movie_user_classes import Graph
import csv

movie_user_graph = Graph()
movies_file = "data/movies.csv"
ratings_file = "data/ratings.csv"


def import_movies(movie_file: str, graph: Graph) -> None:
    """Reads the movie_file and populates graph._movies
    """
    with open(movie_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            movie_id = int(row[0])
            title = row[1]
            movie = Movie(movie_id, title)
            graph.movies[movie_id] = movie


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
            rating = int(float(row[2]))
            curr_user = find_or_add_user(graph, curr_userid)  # Does our dict allocation for us
            add_rating(graph, curr_user, movie_id, rating)


def process_compat_users(graph: Graph) -> None:
    """Finds compatible users for each user in graph, and then updates their user_compats attribute accordingly
    """
    # for each user in userGraph
    #     compatUserIds = getMovieUsers(user.getMovies())
    # // add List as keys to Dict(might need conversion / typecast)
    # userCompats.add(compatUserIds)
    # TODO


def _process_compat_score(graph: Graph) -> None:
    """Compute the compatability scores for each user in the graph
    """
    # TODO
    # Idea: take the average of the differences in score between a user and its compat users
    # A: 1.5 - 5.0 = 3.5
    # B: 2.0 - 3.5 = 1.5
    # (3.5 + 1.5) / 2 = 2.5
    # 4.5 - 2.5 = 2.5 <- final score



def process_movie_recommends(graph: Graph, n: int) -> None:
    """Generates a list of n movie reccommendations for each user in grpah and updates their recommended attribute
    accordingly
    """
    # TODO


def find_or_add_user(graph: Graph, id: int) -> User:
    """Returns the user in graph.users with user_id == id. If such a user does not exist in graph.users, the function
    instead creates a new user with user_id = id, adds it to graph.users, and returns that user
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
    if id in graph.users:
        return graph.users[id]
    else:
        graph.users[id] = User(id)
        return graph.users[id]


def add_rating(graph: Graph, user: User, movieid: int, rating: int) -> None:
    """Adds a rating with movie id and rating to the user's movie_ratings attribute
    and adds a user and its user rating to the movie's user_ratings attribute
    """
    user.movie_ratings[movieid] = rating
    movie = graph.movies[movieid]
    movie.user_ratings[user] = rating


def get_movie_users(movies: list[Movie],users:dict[int,User]) -> set[int]:
    """Returns a set of ids for users who have a rating for at least one movie in movies
    """

    # return userSet
    all_users = []
    for movie in movies:
        all_users.extend(movie.get_users(users))
    user_id_lst = [user.user_id for user in all_users]
    return set(user_id_lst)


if __name__ == '__main__':
    from ui import ui_main
    import_movies(movies_file, movie_user_graph)
    import_ratings(ratings_file, movie_user_graph)
    process_compat_users(movie_user_graph)
    # process_movie_recommends()
    ui_main(movie_user_graph)
