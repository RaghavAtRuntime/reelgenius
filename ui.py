import tkinter as tk
from tkinter import ttk

from movie_user_classes import *

import doctest
import python_ta


def ui_main(graph: Graph):
    root = tk.Tk()

    from random import randint
    user = graph.get_user(randint(1, 5))
    UserPage(root, graph, user)

    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    root.resizable(False, False)
    root.title("ReelGenius")
    root.mainloop()


class UserPage(tk.Frame):
    """ Page displaying the graph data for a user
    """
    _root: tk.Tk
    _graph: Graph
    _user: User
    _searchEntry: ttk.Entry

    def __init__(self, root: tk.Tk, graph: Graph, user: User):
        self._root = root
        self._graph = graph
        self._user = user

        tk.Frame.__init__(self, root, padx=10, pady=10)

        # Row 0
        ttk.Label(self, text="ReelGenius", font=("Helvetica", 15)).grid(row=0, column=0)
        self._searchEntry = ttk.Entry(self)
        self._searchEntry.grid(row=0, column=1)
        ttk.Button(self, command=self._search, text="Search User").grid(row=0, column=2)

        # Row 1
        ttk.Label(self, text=f"User {user.user_id}", font=("Helvetica", 20), padding=10).grid(row=1, column=0)

        # Tabs
        notebook = ttk.Notebook(self)
        notebook.add(RecommendationsFrame(notebook, graph, user), text="Recommendations")
        notebook.add(MyRatingsFrame(notebook, graph, user), text="My Ratings")
        notebook.add(CompatibleUsersFrame(notebook, graph, user), text="Compatible Users")
        # notebook.pack(fill=tk.BOTH, expand=True)
        notebook.grid(row=2, column=0, columnspan=3, sticky='nwes')

        self.pack(fill=tk.BOTH, expand=True)

    def _search(self):
        entry_str = self._searchEntry.get()
        self._searchEntry.delete(0, tk.END)
        if entry_str.isdigit():
            new_user_id = int(entry_str)
            if self._graph.user_exists(new_user_id):
                self._user = self._graph.get_user(new_user_id)
                self._reload()

    def _reload(self):
        self.destroy()
        self._root.update()
        self.__init__(self._root, self._graph, self._user)


class RecommendationsFrame(ttk.Frame):
    """ Frame displaying list of movie recommendations
    """

    def __init__(self, notebook: ttk.Notebook, graph: Graph, user: User):
        ttk.Frame.__init__(self, notebook)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical')
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Treeview
        tree = ttk.Treeview(self, column=("c1", "c2"), show='headings', height=10)
        tree.column("# 1", anchor=tk.CENTER)
        tree.heading("# 1", text="Title")
        tree.column("# 2", anchor=tk.CENTER)
        tree.heading("# 2", text="Rating")

        # for key, value in {x for x in sorted(data.items(), key=lambda item: item[1])}:
        #     star_value = "★" + str(value)
        #     tree.insert('', 'end', text=key, values=(key, star_value))
        for movie_id in user.recommendations:
            movie = graph.get_movie(movie_id)
            cell_1 = movie.title
            cell_2 = '★' + str(movie.user_ratings[user.user_id])
            tree.insert('', 'end', text=cell_1, values=(cell_1, cell_2))
        tree.pack()

        tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.yview)


class MyRatingsFrame(ttk.Frame):
    """ Frame displaying list of movie ratings
    """

    def __init__(self, notebook: ttk.Notebook, graph: Graph, user: User):
        ttk.Frame.__init__(self, notebook)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical')
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Treeview
        tree = ttk.Treeview(self, column=("c1", "c2"), show='headings', height=10)
        tree.column("# 1", anchor=tk.CENTER)
        tree.heading("# 1", text="Title")
        tree.column("# 2", anchor=tk.CENTER)
        tree.heading("# 2", text="Rating")

        # for key, value in data.items():
        #     star_value = "★" + str(value)
        #     tree.insert('', 'end', text=key, values=(key, star_value))
        for movie_id, rating in user.movie_ratings.items():
            movie = graph.get_movie(movie_id)
            cell_1 = movie.title
            cell_2 = str(rating)
            tree.insert('', 'end', text=cell_1, values=(cell_1, cell_2))
        tree.pack()

        tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.yview)


class CompatibleUsersFrame(ttk.Frame):
    """ Frame displaying list of compatible users
    """

    def __init__(self, notebook: ttk.Notebook, graph: Graph, user: User):
        ttk.Frame.__init__(self, notebook)

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient='vertical')
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Treeview
        tree = ttk.Treeview(self, column=("c1", "c2"), show='headings', height=10)
        tree.column("# 1", anchor=tk.CENTER)
        tree.heading("# 1", text="User")
        tree.column("# 2", anchor=tk.CENTER)
        tree.heading("# 2", text="Score")

        # for key, value in data.items():
        #     num_value = "#" + str(value)
        #     tree.insert('', 'end', text=key, values=(key, num_value))
        for user_id, score in user.user_compats.items():
            cell_1 = 'User ' + str(user_id)
            cell_2 = str(score)
            tree.insert('', 'end', text=cell_1, values=(cell_1, cell_2))
        tree.pack()

        tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=tree.yview)


if __name__ == '__main__':
    doctest.testmod()
    python_ta.check_all(config={
        'extra-imports': ['tkinter', 'movie_user_classes', 'doctest', 'random'],
        'allowed-io': [],
        'max-line-length': 120
    })
