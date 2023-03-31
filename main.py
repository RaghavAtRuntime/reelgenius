"""
Main file containing core functions.
mainly focused around passing values to the UI and initializing our Graph and nodes
"""
# Main File

from timeit import default_timer as timer
import doctest
import python_ta

from ui import ui_main
from read_data import import_movies, import_ratings
from graph import Graph

MIN_COMPAT_SCORE = 4.0
MIN_RATING_SCORE = 4.0
RECOMMENDATION_LENGTH = 12

if __name__ == '__main__':
    movie_user_graph = Graph()
    movies_file = "data/movies.csv"
    ratings_file = "data/ratings.csv"

    def load() -> None:
        """Draws loading screen while data is being processed and returned

        """
        start = timer()
        import_movies(movies_file, movie_user_graph)
        print(f'import_movies time: {timer() - start}')

        start = timer()
        import_ratings(ratings_file, movie_user_graph)
        print(f'import_ratings time: {timer() - start}')

        start = timer()
        movie_user_graph.process_compat_users()
        print(f'process_compat_users time: {timer() - start}')

        start = timer()
        movie_user_graph.process_movie_recommends(MIN_COMPAT_SCORE, MIN_RATING_SCORE, RECOMMENDATION_LENGTH)
        print(f'process_movie_recommends time: {timer() - start}')

    ui_main(movie_user_graph, load_fn=load)

    # doctest.testmod()
    # python_ta.check_all(config={
    #     'extra-imports': ['__future__', 'movie_user_classes', 'ui', 'read_data', 'graph', 'csv'],
    #     'allowed-io': [''],
    #     'max-line-length': 120
    # })
