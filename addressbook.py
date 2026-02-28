from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import os

screen = Tk()
screen.title("address book")
screen.geometry("500x500")

#functions

details = {}

def clear():
    nameentry.delete(0,END)
    addressentry.delete(0,END)
    mobileentry.delete(0,END)
    emailentry.delete(0,END)
    birthdayentry.delete(0,END)

def addupdate():
    key = nameentry.get()
    if key == "":
        messagebox.showerror("error!", "please enter a name")
    else:
        if key not in details.keys():
            listbox.insert(END,key)
        details[key]=(addressentry.get(),mobileentry.get(),emailentry.get(),birthdayentry.get())
    clear()
            

#designing

titlelabel = Label(screen,text="address book")
openbutton = Button(screen,text="open")
namelabel = Label(screen,text="name:")
nameentry = Entry(screen)
addresslabel = Label(screen,text="address:")
addressentry = Entry(screen)
mobilelabel = Label(screen,text="mobile:")
mobileentry = Entry(screen)
emaillabel = Label(screen,text="email:")
emailentry = Entry(screen)
birthdaylabel = Label(screen,text="birthday:")
birthdayentry = Entry(screen)
editbutton = Button(screen,text="edit")
deletebutton = Button(screen,text="delete")
updateaddbutton = Button(screen,text="update/add",command=addupdate)
savebutton = Button(screen,text="save")
listbox = Listbox(screen,height=15,width=33)

#gridding
titlelabel.place(x=170,y=20)
openbutton.place(x=270,y=20)
listbox.place(x=30,y=60)
namelabel.place(x=270,y=80)
nameentry.place(x=320,y=80)
addresslabel.place(x=270,y=130)
addressentry.place(x=320,y=130)
mobilelabel.place(x=270,y=180)
mobileentry.place(x=320,y=180)
emaillabel.place(x=270,y=230)
emailentry.place(x=320,y=230)
birthdaylabel.place(x=260,y=280)
birthdayentry.place(x=320,y=280)
editbutton.place(x=70,y=340)
deletebutton.place(x=130,y=340)
updateaddbutton.place(x=300,y=340)
savebutton.place(x=230,y=400)


screen.mainloop()