from tkinter import *

screen=Tk()
screen.geometry("140x110")

spinbox = Spinbox(screen,from_=1,to=10)
spinbox.place(x=5,y=20)

screen.mainloop()
