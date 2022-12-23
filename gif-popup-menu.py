from tkinter import *
from functools import cache
import requests
import json
from urllib.request import urlopen
import time
import _thread
from PIL import Image, ImageTk
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import pyperclip

APIKEY = "LIVDSRZULELA"
LMT = 6
gif_w = 740//2
gif_h = 700//3


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
        
        print("updating")
        gif1 = ImageTk.PhotoImage(Image.open(urlopen(gifs[0]["preview"])).resize((gif_w, gif_h)))
        gif1Label.configure(image=gif1)
        gif1Label.image = gif1

        gif2 = ImageTk.PhotoImage(Image.open(urlopen(gifs[1]["preview"])).resize((gif_w, gif_h)))
        gif2Label.configure(image=gif2)
        gif2Label.image = gif2

        gif3 = ImageTk.PhotoImage(Image.open(urlopen(gifs[2]["preview"])).resize((gif_w, gif_h)))
        gif3Label.configure(image=gif3)
        gif3Label.image = gif3

        gif4 = ImageTk.PhotoImage(Image.open(urlopen(gifs[3]["preview"])).resize((gif_w, gif_h)))
        gif4Label.configure(image=gif4)
        gif4Label.image = gif4

        gif5 = ImageTk.PhotoImage(Image.open(urlopen(gifs[4]["preview"])).resize((gif_w, gif_h)))
        gif5Label.configure(image=gif5)
        gif5Label.image = gif5

        gif6 = ImageTk.PhotoImage(Image.open(urlopen(gifs[5]["preview"])).resize((gif_w, gif_h)))
        gif6Label.configure(image=gif6)
        gif6Label.image = gif6


# Create a text variable for searchbar
var = StringVar()
var.trace_add("write", callback=fetch_top_gifs)

# Create search bar and focus it for quick search
search = Entry(text="", textvariable=var)
search.grid(row=0)
#search.pack()
search.focus()


# Set up top 6 gifs
gif1 = ImageTk.PhotoImage(Image.open(urlopen("https://upload.wikimedia.org/wikipedia/commons/3/3e/Evangelion.png")).resize((gif_w, gif_h)))
gif1Label = Label(ws, image=gif1)
gif1Label.grid(column=0, row=1)

gif2 = ImageTk.PhotoImage(Image.open(urlopen("https://upload.wikimedia.org/wikipedia/commons/3/3e/Evangelion.png")).resize((gif_w, gif_h)))
gif2Label = Label(ws, image=gif2)
gif2Label.grid(column=1, row=1)

gif3 = ImageTk.PhotoImage(Image.open(urlopen("https://upload.wikimedia.org/wikipedia/commons/3/3e/Evangelion.png")).resize((gif_w, gif_h)))
gif3Label = Label(ws, image=gif3)
gif3Label.grid(column=0, row=2)

gif4 = ImageTk.PhotoImage(Image.open(urlopen("https://upload.wikimedia.org/wikipedia/commons/3/3e/Evangelion.png")).resize((gif_w, gif_h)))
gif4Label = Label(ws, image=gif4)
gif4Label.grid(column=1, row=2)

gif5 = ImageTk.PhotoImage(Image.open(urlopen("https://upload.wikimedia.org/wikipedia/commons/3/3e/Evangelion.png")).resize((gif_w, gif_h)))
gif5Label = Label(ws, image=gif5)
gif5Label.grid(column=0, row=3)

gif6 = ImageTk.PhotoImage(Image.open(urlopen("https://upload.wikimedia.org/wikipedia/commons/3/3e/Evangelion.png")).resize((gif_w, gif_h)))
gif6Label = Label(ws, image=gif6)
gif6Label.grid(column=1, row=3)


"""
gif6 = ImageTk.PhotoImage(Image.open(urlopen("https://upload.wikimedia.org/wikipedia/commons/3/3e/Evangelion.png")).resize((gif_w, gif_h)), format="gif")
gif6Label = Label(ws, image=gif6)
gif6Label.grid(column=1, row=3)
"""


ws.mainloop()
