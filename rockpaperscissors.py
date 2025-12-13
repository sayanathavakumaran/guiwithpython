from tkinter import *

screen = Tk()
screen.geometry("600x500")
screen.config(background="maroon")
pscore = 0
cscore = 0
titlelabel = Label(screen,text="rock paper scissors !!",background = "maroon",font=("calibri",15,"bold"),foreground="blanched almond")
titlelabel.place(x=195,y=20)
screen.mainloop()