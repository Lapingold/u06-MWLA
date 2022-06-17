import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests
import json


class Tab9Controller:

    def __init__(self, tab_parent):
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Most Popular Movies")

        self.allLabelTab7 = tk.Label(self.tab, text="Movie Ranking")
        self.buttonCommit = tk.Button(self.tab, text="IMDB:s Most Popular Movies", command=self.cs_movies, activebackground="yellow")

        self.allLabelTab7.grid(row=0, column=0, padx=15, pady=15)
        self.buttonCommit.grid(row=0, column=1, padx=15, pady=15)
    # Define a funktion to use en imdb API that show all the coming soon movies.

    def cs_movies(self):
        # you can find IMDBs API here: https://imdb-api.com/api
        url = "https://imdb-api.com/en/API/MostPopularMovies/k_i4k5g19z"
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        # Get binary format data and convert to jason format
        items = json.loads(response.content)["items"]

        j = 0
        for item in items:
            e = tk.Entry(self.tab, width=100, fg='blue', bg='yellow')
            title = item['title']
            year = item['year']
            rank = item['rank']
            imDbRating = item['imDbRating']
            result = f'Title: {title}. Release: {year}. Rank {rank}. Rating {imDbRating}'
            e.grid(row=j + 5, column=0)
            e.insert(END, result)
            j = j + 1

