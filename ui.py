import tkinter as tk
from tkinter import ttk

from movie_user_classes import *


def ui_main(graph: Graph):
    root = tk.Tk()
    ###
    user = User(1234)
    user.user_id = 1234
    user.movie_ratings = {
        1: 5,
        2: 3.5,
        3: 2.5,
        4: 4,
    }
    user.recommendations = []
    ###
    _user_page(root, user)

    root.columnconfigure(1, weight=1)
    root.rowconfigure(1, weight=1)
    root.resizable(False, False)
    root.title("ReelGenius")
    root.mainloop()


def _user_page(root: tk.Tk, user: User):
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
    notebook.add(_recommendations_frame(notebook), text="Recommendations")
    notebook.add(_my_ratings_frame(notebook), text="My Ratings")
    notebook.add(_compatible_users_frame(notebook), text="Compatible Users")
    #notebook.pack(fill=tk.BOTH, expand=True)
    notebook.grid(row=2, column=0, columnspan=3, sticky='nwes')

    frm.pack(fill=tk.BOTH, expand=True)


def _recommendations_frame(notebook: ttk.Notebook) -> ttk.Frame:
    frm = ttk.Frame(notebook)

    data = {
        "Movie 1": 5,
        "Movie 2": 4,
        "Movie 3": 3,
        "Movie 4": 2,
        "Movie 5": 1,
        "Movie 6": 5,
        "Movie 7": 4,
        "Movie 8": 3,
        "Movie 9": 2,
        "Movie 10": 1,
        "Movie 11": 5,
        "Movie 12": 4,
        "Movie 13": 3,
        "Movie 14": 2,
        "Movie 15": 1,
    }

    # Scrollbar
    scrollbar = ttk.Scrollbar(frm, orient='vertical')
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Treeview
    tree = ttk.Treeview(frm, column=("c1", "c2"), show='headings', height=10)
    tree.column("# 1", anchor=tk.CENTER)
    tree.heading("# 1", text="Title")
    tree.column("# 2", anchor=tk.CENTER)
    tree.heading("# 2", text="Rating")

    for key, value in {x for x in sorted(data.items(), key=lambda item: item[1])}:
        star_value = "★" + str(value)
        tree.insert('', 'end', text=key, values=(key, star_value))
    tree.pack()

    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    return frm

def _compatible_users_frame(notebook: ttk.Notebook) -> ttk.Frame:
    frm = ttk.Frame(notebook)

    data = {
        "User 1": 4,
        "User 2": 4,
        "User 3": 4,
        "User 4": 4,
        "User 5": 4,
    }

    # Scrollbar
    scrollbar = ttk.Scrollbar(frm, orient='vertical')
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Treeview
    tree = ttk.Treeview(frm, column=("c1", "c2"), show='headings', height=10)
    tree.column("# 1", anchor=tk.CENTER)
    tree.heading("# 1", text="User")
    tree.column("# 2", anchor=tk.CENTER)
    tree.heading("# 2", text="#")

    for key, value in data.items():
        num_value = "#" + str(value)
        tree.insert('', 'end', text=key, values=(key, num_value))
    tree.pack()

    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    return frm

def _my_ratings_frame(notebook: ttk.Notebook) -> ttk.Frame:
    frm = ttk.Frame(notebook)

    data = {
        "Movie 1": 5,
        "Movie 2": 4,
        "Movie 3": 3,
        "Movie 4": 2,
        "Movie 5": 1,
        "Movie 6": 5,
        "Movie 7": 4,
        "Movie 8": 3,
        "Movie 9": 2,
        "Movie 10": 1,
        "Movie 11": 5,
        "Movie 12": 4,
        "Movie 13": 3,
        "Movie 14": 2,
        "Movie 15": 1,
    }

    # Scrollbar
    scrollbar = ttk.Scrollbar(frm, orient='vertical')
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    # Treeview
    tree = ttk.Treeview(frm, column=("c1", "c2"), show='headings', height=10)
    tree.column("# 1", anchor=tk.CENTER)
    tree.heading("# 1", text="Title")
    tree.column("# 2", anchor=tk.CENTER)
    tree.heading("# 2", text="Rating")

    for key, value in data.items():
        star_value = "★" + str(value)
        tree.insert('', 'end', text=key, values=(key, star_value))
    tree.pack()

    tree.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)

    return frm