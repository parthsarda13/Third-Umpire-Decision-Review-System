# Import the required library
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")

# Add a Canvas widget
canvas = Canvas(win, background= "yellow")

# Draw a rectangle in Canvas and inherit the background color of Canvas
# canvas.create_rectangle(50,50,350,190, outline="black", fill= canvas["background"])
canvas.pack()
win.mainloop()