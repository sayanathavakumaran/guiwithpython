from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("500x300")


def multiplication():
    table = ""
    radiovalue = radiobuttonvalues.get()
    for x in range(radiovalue+1):
        


title = Label(screen,text="multiplication table")
title.place(x=210,y=30)

dropboxlabel = Label(screen,text="number:")
dropboxlabel.place(x=50,y=100)

comboboxvalues = IntVar()

dropbox = Combobox(screen,textvariable=comboboxvalues,width=15)
dropbox["values"]=tuple(range(101))
dropbox.place(x=130,y=100)

radiobuttonvalues = IntVar()

radiobutton = Radiobutton(screen,text="5",variable=radiobuttonvalues,value=5)
radiobutton.place(x=380,y=100)
radiobutton2 = Radiobutton(screen,text="10",variable=radiobuttonvalues,value=10)
radiobutton2.place(x=380,y=130)
radiobutton3 = Radiobutton(screen,text="15",variable=radiobuttonvalues,value=15)
radiobutton3.place(x=380,y=160)

submit = Button(screen,text="submit")
submit.place(x=220,y=200)

screen.mainloop()