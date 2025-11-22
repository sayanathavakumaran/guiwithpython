from tkinter import *

screen = Tk()
screen.config(background="lavender")


def convert():
    entryboxstore = kgentry.get()
    entryboxstore = float(entryboxstore)
    #kg to grams
    gramvalue = entryboxstore*1000
    #kg to pounds
    poundvalue = entryboxstore*2.20462
    #kg to ounces
    ouncevalue = entryboxstore*35.274
    gramtext.delete("1.0",END)
    poundtext.delete("1.0",END)
    ouncetext.delete("1.0",END)
    gramtext.insert(END,gramvalue)
    poundtext.insert(END,poundvalue)
    ouncetext.insert(END,ouncevalue)


#defining widgets

enterlabel = Label(screen,text="enter your weight in kg  ",background="lavender",font=("calibri",13))
gramlabel = Label(screen,text="grams",background="lavender",font=("calibri",13))
poundslabel = Label(screen,text="pounds",background="lavender",font=("calibri",13))
ouncelabel = Label(screen,text="ounces",background="lavender",font=("calibri"))
kgentry = Entry(screen,text="",font=("calibri",13))
convertbutton = Button(screen,text="convert",font=("calibri",13),command=convert)
gramtext = Text(screen,height=1,width=15)
poundtext = Text(screen,height=1,width=15)
ouncetext = Text(screen,height=1,width=15)

#placing the widgets

enterlabel.grid(row=0,column=0)
kgentry.grid(row=0,column=1)
convertbutton.grid(row=0,column=2)
gramlabel.grid(row=1,column=0)
poundslabel.grid(row=1,column=1)
ouncelabel.grid(row=1,column=2)
gramtext.grid(row=2,column=0)
poundtext.grid(row=2,column=1)
ouncetext.grid(row=2,column=2)

screen.mainloop()