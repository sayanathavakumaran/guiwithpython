from tkinter import *
import random
from tkinter import messagebox

screen = Tk()
screen.geometry("500x500")
screen.config(background="#530707")

wwords = ["albania","dubai","spain","france","somalia","kuwait","uruguay","latvia","srilanka","hungary","botswana","seychelles","bermuda","australia","cambodia","germany","sweden","ukraine","switzerland","vietnam"]
jwords = ["nlaaiba","iabdu","pains","cnafer","laisamo","tiwaku","yraauug","avlati","narsilka","nyhruar","asbnotwo","cseyhselel","damrube","tsauarlia","badcmaoi","mnygare","edwnes","kraiune","tzlwsardein","mevitan"]

listlen = len(wwords)
choice = random.randint(0,listlen-1)

#gaming variables
canswered = 0
totattempts = 0
scoree = ""

#reset function

def reset():
    global jwords,choice
    choice = random.randint(0,listlen-1)
    word1()
    entrybox.delete(0,END)

#function for initial word
def word1():
    global jwords,choice,wwords
    word.config(text=jwords[choice])

def check():
    global jwords,wwords,choice,canswered,totattempts
    totattempts+=1
    userentry = entrybox.get()
    if userentry == wwords[choice]:
        canswered+=1
        messagebox.showinfo("alert !!","that is correct !!")
    else:
        messagebox.showinfo("alert !!","oops, that's not right...")
    reset()
    scoree = "score: "+str(canswered)+"/"+str(totattempts)
    score.config(text=scoree)



title = Label(screen,text="jumbled country game !!", background = "#530707", font = ("calibri",19),foreground="#FFF0B3")
title.place(x=130,y=40)


word = Label(screen,text="---", background = "#530707", font = ("calibri",14),foreground="#FFF0B3")
word.place(x=215,y=120)

entrybox = Entry(screen)
entrybox.place(x=190,y=195)


checkbutton = Button(screen,text=" check ",background = "#681515",foreground="#FFF0B3",font=("calibri",13),command=check)
checkbutton.place(x=220,y=280)

resetbutton = Button(screen,text="reset",background = "#681515",foreground="#FFF0B3",font=("calibri",13),command=reset)
resetbutton.place(x=227,y=360)

score = Label(screen, background = "#530707", font = ("calibri",14),foreground="#FFF0B3")
score.place(x=38,y=390)

word1()

screen.mainloop()
