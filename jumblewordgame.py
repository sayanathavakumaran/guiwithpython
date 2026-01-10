from tkinter import *
import random
from tkinter import messagebox

screen = Tk()
screen.geometry("500x500")
screen.config(background="#530707")




title = Label(screen,text="jumbled word game !!", background = "#530707", font = ("calibri",19),foreground="#FFF0B3")
title.place(x=140,y=40)


word = Label(screen,text="444", background = "#530707", font = ("calibri",14),foreground="#FFF0B3")
word.place(x=230,y=120)


entrybox = Entry(screen)
entrybox.place(x=190,y=195)


checkbutton = Button(screen,text=" check ",background = "#681515",foreground="#FFF0B3",font=("calibri",15))
checkbutton.place(x=215,y=280)

submitbutton = Button(screen,text="submit",background = "#681515",foreground="#FFF0B3",font=("calibri",15))
submitbutton.place(x=210,y=360)

score = Label(screen,text="", background = "#530707", font = ("calibri",15),foreground="#FFF0B3")
score.place(x=35,y=390)

screen.mainloop()