from tkinter import *
from functools import cache
import requests
import json

APIKEY = "LIVDSRZULELA"
LMT = 8


ws = Tk()
ws.title("Gif menu")
ws.geometry("750x750")  
ws.resizable(0, 0)            



gifs = []

@cache
def call_tenor_api(search_str):
    return requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_str, APIKEY, LMT))


def fetch_top_gifs(search_str, h, j):
    """
    Gets the top gifs from Tenor's API, updates a list that contains
    gif data.

    """
    global gifs

    r = call_tenor_api(search_str)

    if r.status_code == 200:
        # successful api call
        tenor_gifs = json.loads(r.content)['results']
        tenor_gifs = [x['media'][0]['gif'] for x in tenor_gifs]
        gifs = tenor_gifs
        print("gifs")

# Create a text variable for searchbar
var = StringVar()
var.trace_add("write", callback=fetch_top_gifs)

# Create search bar and focus it for quick search
search = Entry(text="", textvariable=var)
search.pack()
search.focus()


ws.mainloop()
