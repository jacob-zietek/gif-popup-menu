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
APIKEY = "LIVDSRZULELA"
LMT = 8


ws = Tk()
ws.title("Gif menu")
ws.geometry("750x750")  
ws.resizable(0, 0)            

gifs = []

class gifplay:
    """
    Usage: mygif=gifplay(<<tkinter.label Objec>>,<<GIF path>>,<<frame_rate(in ms)>>)
    example:
    gif=GIF.gifplay(self.model2,'./res/neural.gif',0.1)
    gif.play()
    This will play gif infinitely

    source: https://gist.github.com/gupta-shantanu/8781f72ff903c2cf3878
    """
    def __init__(self,label,gif_url,delay=0.1):
        self.frame=[]
        i=0

        image_data = Image.open(urlopen(gif_url)).resize((gif_w, gif_h))

        while 1:
            try:
                image=ImageTk.PhotoImage(image_data, format="gif -index "+str(i))
                self.frame.append(image)
                i=i+1
            except:
                break
        print(i)
        self.totalFrames=i-1
        self.delay=delay
        self.labelspace=label
        self.labelspace.image=self.frame[0]

    def play(self):
        """
        plays the gif
        """
        _thread.start_new_thread(self.infinite,())

    def infinite(self):
        i=0
        while 1:
            self.labelspace.configure(image=self.frame[i])
            i=(i+1)%self.totalFrames
            time.sleep(self.delay)

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
search.grid(row=0)
#search.pack()
search.focus()

gif_w = 740//2
gif_h = 700//3
# Set up top 6 gifs
gif1 = ImageTk.PhotoImage(Image.open(urlopen("https://media.tenor.com/846fTf5uEgcAAAAC/bfb-bfdi.gif")).resize((gif_w, gif_h)), format="gif")
gif1Label = Label(ws, image=gif1)
gif1Label.grid(column=0, row=1)

gif2 = ImageTk.PhotoImage(Image.open(urlopen("https://media.tenor.com/846fTf5uEgcAAAAC/bfb-bfdi.gif")).resize((gif_w, gif_h)), format="gif")
gif2Label = Label(ws, image=gif2)
gif2Label.grid(column=1, row=1)

gif3 = ImageTk.PhotoImage(Image.open(urlopen("https://media.tenor.com/846fTf5uEgcAAAAC/bfb-bfdi.gif")).resize((gif_w, gif_h)), format="gif")
gif3Label = Label(ws, image=gif3)
gif3Label.grid(column=0, row=2)

gif4 = ImageTk.PhotoImage(Image.open(urlopen("https://media.tenor.com/846fTf5uEgcAAAAC/bfb-bfdi.gif")).resize((gif_w, gif_h)), format="gif")
gif4Label = Label(ws, image=gif4)
gif4Label.grid(column=1, row=2)

gif5 = ImageTk.PhotoImage(Image.open(urlopen("https://media.tenor.com/846fTf5uEgcAAAAC/bfb-bfdi.gif")).resize((gif_w, gif_h)), format="gif")
gif5Label = Label(ws, image=gif5)
gif5Label.grid(column=0, row=3)

gif6 = ImageTk.PhotoImage(Image.open(urlopen("https://media.tenor.com/846fTf5uEgcAAAAC/bfb-bfdi.gif")).resize((gif_w, gif_h)), format="gif")
gif6Label = Label(ws, image=gif6)
gif6Label.grid(column=1, row=3)



ws.mainloop()
