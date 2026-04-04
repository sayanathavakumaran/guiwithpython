from tkinter import *
from tkinter.colorchooser import askcolor

#default settings
pensizedefault = 4.0
colourdefault = "black"

#global variables
x = None
y = None
colour = colourdefault
eraseron = False
activebutton = None
linewidth = pensizedefault

#functions
def activate(btn):
    global activebutton
    if activebutton == True:
        activebutton.config(relief=RAISED)
    btn.config(relief=SUNKEN)
    activebutton=btn

#designing
screen = Tk()
screen.title("painting app")

#buttons
pen = Button(screen,text="pen")
brush = Button(screen,text="brush")
colour = Button(screen,text="colour")
eraser = Button(screen,text="eraser")
slider = Scale(screen,from_=1,to=10,orient=HORIZONTAL)

pen.grid(row=0,column=0)
brush.grid(row=0,column=1)
colour.grid(row=0,column=2)
eraser.grid(row=0,column=3)
slider.grid(row=0,column=4)

#canvas
canvas = Canvas(screen,bg="white",width=400,height=400)
canvas.grid(row=1,columnspan=5)



screen.mainloop()