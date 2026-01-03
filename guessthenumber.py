from tkinter import *
import random

screen = Tk()
screen.geometry("500x400")
screen.config(background="pale turquoise")

compnumber = random.randint(1,100)
attempts = 0

def submit():
    global compnumber
    global attempts
    attempts += 1
    guessentryi = guessentry.get()
    guessentryi = int(guessentryi)
    if guessentryi < compnumber:
        cluelabel.config(text="too low !!")
    elif guessentryi > compnumber:
        cluelabel.config(text="too high !!")
    elif guessentryi == compnumber:
        cluelabel.config(text="well done !!")
        attemptslabel.config(text="attempts: "+str(attempts))



def reset():
    guessentry.delete(0,END)
    cluelabel.config(text="")
    


titlelabel = Label(screen,text="guess the number !! (1-100)",background="pale turquoise",font=("calibri",15,"bold"),foreground="dark cyan")
titlelabel.place(x=135,y=20)
titlelabel2 = Label(screen,text="guess a number between 1 and 100",background="pale turquoise",font=("calibri",12),foreground="dark cyan")
titlelabel2.place(x=138,y=65)
attemptslabel = Label(screen,text="", background = "pale turquoise", font = ("calibri",12),foreground = "dark cyan")
attemptslabel.place(x=200,y=110)
cluelabel = Label(screen,background="pale turquoise",font=("calibri",11),foreground="dark cyan")
cluelabel.place(x=200,y=135)
guessentry = Entry(screen)
guessentry.place(x=185,y=185)
submitbutton = Button(screen,text="submit",background="light green",font=("calibri",10),foreground="dark green",command=submit)
submitbutton.place(x=220,y=250)
resetbutton = Button(screen,text="reset",background="light salmon",font=("calibri",10),foreground="maroon",command=reset)
resetbutton.place(x=225,y=305)


screen.mainloop()
