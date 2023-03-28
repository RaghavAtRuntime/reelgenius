import tkinter as tk
from tkinter import ttk

from movie_user_classes import *


def ui_main(graph: Graph):
    root = tk.Tk()

    from random import randint
    user = graph.get_user(randint(1, 100))
    _user_page(root, graph, user)

    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    root.resizable(False, False)
    root.title("ReelGenius")
    root.mainloop()


def _user_page(root: tk.Tk, graph: Graph, user: User):
    # Frame
    frm = tk.Frame(root, padx=10, pady=10)

    # Row 0
    ttk.Label(frm, text="ReelGenius", font=("Helvetica", 15)).grid(row=0, column=0)
    ttk.Entry(frm).grid(row=0, column=1)
    ttk.Button(frm, text="Search User").grid(row=0, column=2)

    # Row 1
    ttk.Label(frm, text=f"User: {user.user_id}", font=("Helvetica", 20), padding=10).grid(row=1, column=0)

    # Tabs
    notebook = ttk.Notebook(frm)
    notebook.add(_recommendations_frame(notebook, graph, user), text="Recommendations")
    notebook.add(_my_ratings_frame(notebook, graph, user), text="My Ratings")
    notebook.add(_compatible_users_frame(notebook, graph, user), text="Compatible Users")
    # notebook.pack(fill=tk.BOTH, expand=True)
    notebook.grid(row=2, column=0, columnspan=3, sticky='nwes')

    frm.pack(fill=tk.BOTH, expand=True)


def _recommendations_frame(notebook: ttk.Notebook, graph: Graph, user: User) -> ttk.Frame:
    frm = ttk.Frame(notebook)

    # Scrollbar
    scrollbar = ttk.Scrollbar(frm, orient='vertical')
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Treeview
    tree = ttk.Treeview(frm, column=("c1", "c2"), show='headings', height=10)
    tree.column("# 1", anchor=tk.CENTER)
    tree.heading("# 1", text="Title")
    tree.column("# 2", anchor=tk.CENTER)
    tree.heading("# 2", text="Rating")

    # for key, value in {x for x in sorted(data.items(), key=lambda item: item[1])}:
    #     star_value = "★" + str(value)
    #     tree.insert('', 'end', text=key, values=(key, star_value))
    for movie_id in user.recommendations:
        movie = graph.movies[movie_id]
        cell_1 = movie.title
        cell_2 = '★' + str(movie.user_ratings[user.user_id])
        tree.insert('', 'end', text=cell_1, values=(cell_1, cell_2))
    tree.pack()

    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    return frm


def _my_ratings_frame(notebook: ttk.Notebook, graph: Graph, user: User) -> ttk.Frame:
    frm = ttk.Frame(notebook)

    # Scrollbar
    scrollbar = ttk.Scrollbar(frm, orient='vertical')
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Treeview
    tree = ttk.Treeview(frm, column=("c1", "c2"), show='headings', height=10)
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

    return frm


def _compatible_users_frame(notebook: ttk.Notebook, graph: Graph, user: User) -> ttk.Frame:
    frm = ttk.Frame(notebook)

    # Scrollbar
    scrollbar = ttk.Scrollbar(frm, orient='vertical')
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Treeview
    tree = ttk.Treeview(frm, column=("c1", "c2"), show='headings', height=10)
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

    return frm
