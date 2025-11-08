from tkinter import *

screen = Tk()

screen.geometry("500x500")
screen.config(background="powderblue")

def enter():
    username1 = userbox.get()
    password1 = passbox.get()
    userfile = open("userinfo.txt","a")
    userfile.write(f"username:{username1},password:{password1}\n")
    userbox.delete(0,END)
    passbox.delete(0,END)


username = Label(screen,text="username",background="light grey",font = ("calibri",(9)))
username.place(x=100,y=90)
password = Label(screen,text="password",background="light grey",font = ("calibri",(9)))
password.place(x=100,y=140)

userbox = Entry(screen,text="",background = "light grey",font = ("calibri",(9)))
userbox.place(x=205,y=90)
passbox = Entry(screen,text="",show="*",background = "light grey",font = ("calibri",(9)))
passbox.place(x=205,y=140)

submit = Button(screen,text="submit",background="light grey",font = ("calibri",(9)),command=enter)
submit.place(x=100,y=215)



screen.mainloop()