from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("600x600")
screen.config(background="misty rose")

#labels

email = Label(screen,text="email",font=("calibri",13))
email.place(x=60,y=50)
password = Label(screen,text="password",font=("calibri",13))
password.place(x=60,y=110)

screen.mainloop()