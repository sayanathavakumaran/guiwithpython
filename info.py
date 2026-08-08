from tkinter import *

screen = Tk()

screen.geometry("700x400")

number = 0
def errorcheck():
    global number
    name1 = namebox.get()
    name2 = name1.replace(" ","")
    age1 = agebox.get()
    if not name2.isalpha():
        print("invalid name")
        number = 1
    if not age1.isdigit():
        print("invalid age")
        number = 1
    submita()
def submita():
    global number
    if number == 0:
        lname = namebox.get()
        lage = agebox.get()
        lnati = natibox.get()
        lemail = emailbox.get()
        listbox.insert(0,"name: "+lname)
        listbox.insert(1,"age: "+lage)
        listbox.insert(2,"nationality: "+lnati)
        listbox.insert(3,"email: "+lemail)

name = Label(screen,text="name")
name.place(x=60,y=90)
age = Label(screen,text="age")
age.place(x=60,y=120)
nati = Label(screen,text="nationality")
nati.place(x=60,y=150)
email = Label(screen,text="email")
email.place(x=60,y=180)

namebox = Entry(screen,text="",background="light grey")
namebox.place(x=150,y=90)
agebox = Entry(screen,text="",background="light grey")
agebox.place(x=150,y=120)
natibox = Entry(screen,text="",background="light grey")
natibox.place(x=150,y=150)
emailbox = Entry(screen,text="",background="light grey")
emailbox.place(x=150,y=180)

submit = Button(screen,text="submit",background="light grey",command=errorcheck)
submit.place(x=135,y=260)
listbox = Listbox(screen,height=15,width=35)
listbox.place(x=400,y=70)
screen.mainloop()