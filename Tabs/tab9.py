import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests
import json
import database


class Tab9Controller:

    def __init__(self, tab_parent):
        self.tab = ttk.Frame(tab_parent)
        tab_parent.add(self.tab, text="Search")
        self.movie1 = tk.StringVar()
        self.movie_id = tk.StringVar()

        self.idLabelTab9 = tk.Label(self.tab, text="Movie name:")
        self.rateLabelTab9 = tk.Label(self.tab, text="Movie Id in IMDB website:")
        
        self.idEntryTab9 = tk.Entry(self.tab, textvariable=self.movie1)
        self.rateEntryTab9 = tk.Entry(self.tab, textvariable=self.movie_id)
        
        tk.Button(self.tab, text="Get movie Id", command=self.id_movies, activebackground="yellow").grid(row=2, column=1, padx=15, pady=15)
        tk.Button(self.tab, text="Get movie rate", command=self.rate_movies, activebackground="yellow").grid(row=4, column=1, padx=15, pady=15)
        
        self.idLabelTab9.grid(row=1, column=0, padx=15, pady=15)
        self.rateLabelTab9.grid(row=3, column=0, padx=15, pady=15)

        self.idEntryTab9.grid(row=1, column=1, padx=15, pady=15)
        self.rateEntryTab9.grid(row=3, column=1, padx=15, pady=15)


    # Define a funktion to use en imdb API that show all the coming soon movies.


    def id_movies(self):
        movie1 = str(self.movie1.get())

        # you can find IMDBs API here: https://imdb-api.com/api
        url = f"https://imdb-api.com/en/API/SearchTitle/k_i4k5g19z/{movie1}"
        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        # Get binary format data and convert to jason format
        items = json.loads(response.content)["results"]

        j = 0
        for item in items:
            e = tk.Entry(self.tab, width=100, fg='blue')
            id_movie = item["id"]
            title = item["title"]
            release_date = item["description"]
            result = f'{id_movie} - {release_date} - {title}'
            e.grid(row=j + 5, column=0)
            e.insert(END, result)
            j = j + 1
        self.idEntryTab9.delete(0, END)

    def rate_movies(self):
        # you can find IMDBs API here: https://imdb-api.com/api
        movie_id = str(self.movie_id.get())
        url = f"https://imdb-api.com/en/API/Ratings/k_i4k5g19z/{movie_id}"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        # Get binary format data and convert to jason format
        items = json.loads(response.content)["imDb"]
        e = tk.Entry(self.tab, width=5, fg='blue')
        e.grid(row=5, column=1)
        e.insert(END, items)

        self.rateEntryTab9.delete(0, END)

    # def name_movies(self):
    #     # you can find IMDBs API here: https://imdb-api.com/api
    #     movie_id = str(self.movie_id.get())
    #     url = f"https://imdb-api.com/en/API/Ratings/k_i4k5g19z/{movie_id}"

    #     payload = {}
    #     headers = {}

    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     # Get binary format data and convert to jason format
    #     items = json.loads(response.content)["imDb"]
    #     e = tk.Entry(self.tab, width=5, fg='blue')
    #     e.grid(row=5, column=1)
    #     e.insert(END, items)

    #     self.rateEntryTab9.delete(0, END)