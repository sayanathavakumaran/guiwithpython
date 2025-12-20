from tkinter import *
import random

screen = Tk()
screen.geometry("500x400")
screen.config(background="misty rose")

titlelabel = Label(screen,text="guess the number !! (1-100)",background="misty rose",font=("calibri",15,"bold"),foreground="maroon")
titlelabel.place(x=135,y=20)
titlelabel2 = Label(screen,text="guess a number between 1 and 100",background="misty rose",font=("calibri",11),foreground="maroon")
titlelabel2.place(x=138,y=65)
entrybox = Entry(screen)
entrybox.place(x=180,y=130)


screen.mainloop()