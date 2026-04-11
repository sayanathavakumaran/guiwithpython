from tkinter import *
from tkinter.colorchooser import askcolor

#default settings
pensizedefault = 4.0
colourdefault = "black"

#global variables
x = None
y = None
color = colourdefault
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

#function for pen tool
def penn():
    global activebutton, eraseron
    activate(pen)
    eraseron = False

def brushh():
    global activebutton, eraseron
    activate(brush)
    eraseron = False

def cchoose():
    global color, eraseron
    eraseron = False
    colourr = askcolor(color=color)[1]
    if colourr:
        color = colourr

def erase():
    global eraseron
    eraseron = True
    activate(eraser)

def reset(event):
    global x, y
    x, y = None, None

def paint(event):
    global x, y, color
    size = slider.get()
    if activebutton == brush:
        width = size*3
    else:
        width = size
    paintcolour = "white" if eraseron else color
    if x and y:
        canvas.create_line(x,y,event.x,event.y,width=width,fill=paintcolour,capstyle=ROUND,smooth=TRUE,splinesteps=35)
    x,y= event.x,event.y



#designing
screen = Tk()
screen.title("painting app")

#buttons
pen = Button(screen,text="pen",command=penn)
brush = Button(screen,text="brush",command=brushh)
colour = Button(screen,text="colour",command=cchoose)
eraser = Button(screen,text="eraser",command=erase)
slider = Scale(screen,from_=1,to=10,orient=HORIZONTAL)

pen.grid(row=0,column=0)
brush.grid(row=0,column=1)
colour.grid(row=0,column=2)
eraser.grid(row=0,column=3)
slider.grid(row=0,column=4)

#canvas
canvas = Canvas(screen,bg="white",width=400,height=400)
canvas.grid(row=1,columnspan=5)
canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>",reset)

activate(pen)
screen.mainloop()
