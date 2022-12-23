from tkinter import *

ws = Tk()
ws.title("Gif menu")
ws.geometry("750x750")  
ws.resizable(0, 0)            

# Create search bar and focus it for quick search
search = Entry(text="")
search.pack()
search.focus()

ws.mainloop()
