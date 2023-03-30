# Main File


from movie_user_classes import User
from movie_user_classes import Movie
from movie_user_classes import Graph
import csv

from timeit import default_timer as timer
from ui import ui_main

movie_user_graph = Graph()
movies_file = "data/movies.csv"
ratings_file = "data/ratings.csv"

MAX_RECOMMENDS = 10
MIN_COMPAT_SCORE = 4
MIN_RATING_SCORE = 4

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
            curr_user = _find_or_add_user(graph, curr_userid)  # Does our dict allocation for us
            add_rating(graph, curr_user, movie_id, rating)


def _find_or_add_user(graph: Graph, user_id: int):
    """Returns the user in graph.users with user_id == id. If such a user does not exist in graph.users, the function
    instead creates a new user with user_id = id, adds it to graph.users, and returns that user
    """
    if not graph.user_exists(user_id):
        graph.add_user(User(user_id))
    return graph.get_user(user_id)


def process_compat_users(graph: Graph) -> None:
    """Finds compatible users for each user in graph, and then updates their user_compats attribute accordingly
    """
    total_compat_users = 0
    for user in graph.get_all_users():
        user_rated_movies = user.get_movies()
        compat_user_ids = get_movie_users(user_rated_movies, graph)
        compat_user_ids.remove(user.user_id)
        total_compat_users += len(compat_user_ids)
        _process_compat_score(graph, user, compat_user_ids)


def _process_compat_score(graph: Graph, user: User, compat_user_ids: set[int]) -> None:
    """Compute the compatability scores between user, and all users with ids in compat_user_ids, and update
    user.user_compats accordingly

    Preconditions:
    - graph.user_exists(user.user_id)
    - all({graph.user_exists(id) for id in compat_user_ids})
    """
    for user_id in compat_user_ids:
        user2 = graph.get_user(user_id)
        user1_movies = user.get_movies()
        user2_movies = user2.get_movies()
        shared_movies = user1_movies.intersection(user2_movies)
        compat_score_so_far = 0.0
        for movie_id in shared_movies:
            user1_rating = user.get_rating(movie_id)
            user2_rating = user2.get_rating(movie_id)
            compat_score_so_far += abs(user1_rating - user2_rating)
        compat_score_so_far = compat_score_so_far / len(shared_movies)
        compat_score_so_far = 4.5 - compat_score_so_far
        user.user_compats[user_id] = compat_score_so_far


def process_movie_recommends(graph: Graph) -> None:
    """Generates a list of n movie reccommendations for each user in grpah and updates their recommended attribute
    accordingly

    Idea:
    - multiply the score each compatible user gives by its comapt rating to the desired user
    """
    for user in graph.get_all_users():  # loops through all users
        recommendation_list = []
        compat_list = sorted(user.user_compats.items(), key=lambda x: x[1], reverse=True)
        for compat in compat_list:
            uid = compat[0]
            comp_score = compat[1]

            #temp
            if(comp_score < MIN_COMPAT_SCORE):
                continue

            compat_user = _find_or_add_user(graph, uid)
            score_list = _get_recommendation_scores(comp_score, compat_user.movie_ratings)
            recommendation_list.extend(score_list)
        sorted_tuples = sorted(recommendation_list, key=lambda x: x[1], reverse=True)
        final_list = [x[0] for x in sorted_tuples]
        user.recommendations = _remove_duplicates(final_list)

        #temp
        if(len(user.recommendations) < 10):
            print(f'User: {user.user_id} recomendLen: {len(user.recommendations)}')


def _remove_duplicates(lst: list[str]) -> list[str]:
    """Remove duplicates from a list, but keep the first occurrence of each item."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
            if len(result) == MAX_RECOMMENDS:
                break
    return result


def _get_recommendation_scores(comp_score: float, movie_ratings: dict[int, float]) -> list[(int, float)]:
    """
    Given the user rating between a user and its compatible user, and the movie_dict of that compatible user, calculate
    the recommendation scores for each movie in the movie_dict by multiplying the ratings in the dict by the given user
    rating. Return a list of tuples containing the movie ID and its recommendation score.
    """
    rec_list = []
    for k in movie_ratings:
        rating_value = movie_ratings[k]

        # temp
        if (rating_value < MIN_RATING_SCORE):
            continue

        rec_score = rating_value * comp_score
        rec_list.append((k, rec_score))
    return rec_list


def add_rating(graph: Graph, user: User, movie_id: int, rating: float) -> None:
    """Adds a rating with movie id and rating to the user's movie_ratings attribute
    and adds a user and its user rating to the movie's user_ratings attribute
    """
    user.movie_ratings[movie_id] = rating
    movie = graph.get_movie(movie_id)
    movie.user_ratings[user.user_id] = rating


def get_movie_users(movies: set[int], graph: Graph) -> set[int]:
    """Returns a set of ids for users in graph who have a rating for at least one movie whose id is in movies

    Preconditions:
    - all({i in graph._movies for i in movies})
    """
    user_ids_so_far = []
    for movie_id in movies:
        user_ids_so_far.extend(graph.get_movie(movie_id).get_users())
    return set(user_ids_so_far)


if __name__ == '__main__':

    def load():
        start = timer()
        import_movies(movies_file, movie_user_graph)
        print(f'import_movies time: {timer() - start}')

        start = timer()
        import_ratings(ratings_file, movie_user_graph)
        print(f'import_ratings time: {timer() - start}')

        start = timer()
        process_compat_users(movie_user_graph)
        print(f'process_compat_users time: {timer() - start}')

        start = timer()
        process_movie_recommends(movie_user_graph)
        print(f'process_movie_recommends time: {timer() - start}')

    ui_main(movie_user_graph, load_fn=load)
