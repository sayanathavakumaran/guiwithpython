from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import os,ast

screen = Tk()
screen.title("address book")
screen.geometry("500x500")

#functions

details = {}

def clearr():
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
    clearr()
            
def edit():
    clearr()
    selected = listbox.curselection()
    if selected:
        nameentry.insert(0,listbox.get(selected))
        alldetails = details[nameentry.get()]
        addressentry.insert(0,alldetails[0])
        mobileentry.insert(0,alldetails[1])
        emailentry.insert(0,alldetails[2])
        birthdayentry.insert(0,alldetails[3])
    else:
        messagebox.showerror("error!","please enter something to edit")
        
def vieww(event):
    screenn = Toplevel(screen)
    selected = listbox.curselection()
    stringeddetails = ""
    if selected:
        name = listbox.get(selected)
        stringeddetails = "name: " + name + "\n"
        alldetails = details[name]
        stringeddetails += "address: " + alldetails[0] + "\n"
        stringeddetails += "mobile: " + alldetails[1] + "\n"
        stringeddetails += "email: " + alldetails[2] + "\n"
        stringeddetails += "birthday: " + alldetails[3]
    viewstrings = Label(screenn)
    viewstrings.grid(row=0,column=0)
    viewstrings.configure(text=stringeddetails)
    

def delete():
    selected = listbox.curselection()
    if selected:
        del details[listbox.get(selected)]
        listbox.delete(selected)
        clearr()
    else:
        messagebox.showerror("error!","select something to delete")

def reset():
    clearr()
    listbox.delete(0,END)
    details.clear()

def save():
    txt = asksaveasfile(defaultextension=".txt")
    if txt:
        print(details,file=txt)
        reset()
    else:
        messagebox.showerror("error!","address book is not saved")

def open():
    reset()
    dialogbox = askopenfile(title="open a file")
    if dialogbox:
        details = ast.literal_eval(dialogbox.read())
        for key in details.keys():
            listbox.insert(END,key)
        titlelabel.configure(text=os.path.basename(dialogbox.name()))

#designing

titlelabel = Label(screen,text="address book")
openbutton = Button(screen,text="open",command=open)
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
editbutton = Button(screen,text="edit",command=edit)
deletebutton = Button(screen,text="delete",command=delete)
updateaddbutton = Button(screen,text="update/add",command=addupdate)
savebutton = Button(screen,text="save",command=save)
listbox = Listbox(screen,height=15,width=33)

#gridding

titlelabel.place(x=170,y=20)
openbutton.place(x=270,y=20)
listbox.place(x=30,y=60)
listbox.bind('<<ListboxSelect>>',vieww)
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
