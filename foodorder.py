from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("700x600")
screen.config(background="light yellow")

def record():
    foodd = foodbox.get()
    drinkss = drinkbox.get()
    dessertss = dessertbox.get()
    foodnum = foodspinbox.get()
    drinknum = drinkspinbox.get()
    dessertnum = dessertspinbox.get()
    userfile = open("foodorders.txt","a")
    userfile.write(f"food:{foodd} , quantity:{foodnum} , drink:{drinkss} , quantity:{drinknum} , dessert:{dessertss}, quantity:{dessertnum}\n")
    foodbox.delete(0,END)
    foodspinbox.delete(0,END)
    dessertbox.delete(0,END)
    dessertspinbox.delete(0,END)
    drinkbox.delete(0,END)
    drinkspinbox.delete(0,END)
    emailbox.delete(0,END)
    passwordbox.delete(0,END)

def progressing():
    import time
    progressbar["value"]=20
    screen.update_idletasks()
    time.sleep(1)
    progressbar["value"]=40
    screen.update_idletasks()
    time.sleep(1)
    progressbar["value"]=60
    screen.update_idletasks()
    time.sleep(1)
    progressbar["value"]=80
    screen.update_idletasks()
    time.sleep(1)
    progressbar["value"]=100

def both():
    record()
    progressing()
    exit()

#labels

email = Label(screen,text="email",background="light yellow",font=("calibri",13))
email.place(x=90,y=50)
password = Label(screen,text="password",background="light yellow",font=("calibri",13))
password.place(x=60,y=110)
foodq = Label(screen,text="what food would you like to order: pasta, pizza, salad, rice or sandwich?",background="lightyellow",font=("calibri",13))
foodq.place(x=90,y=200)
drinkq = Label(screen,text="what drink would you like to order: dr pepper, cola, fanta, orange juice or water?",background="lightyellow",font=("calibri",13))
drinkq.place(x=70,y=300)
dessertq = Label(screen,text="what dessert would you like to order: ice cream, vanilla sponge, brownie or cookie?",background="lightyellow",font=("calibri",13))
dessertq.place(x=60,y=400)

#entry boxes
emailbox = Entry(screen,text="",font=("calibri",13))
emailbox.place(x=200,y=50)
passwordbox = Entry(screen,text="",show="*",font=("calibri",13))
passwordbox.place(x=200,y=110)
foodbox = Entry(screen,text="",font=("calibri",13))
foodbox.place(x=100,y=245)
drinkbox = Entry(screen,text="",font=("calibri",13))
drinkbox.place(x=100,y=345)
dessertbox = Entry(screen,text="",font=("calibri",13))
dessertbox.place(x=100,y=445)

#spinboxes

foodspinbox = Spinbox(screen,from_=0,to=float("inf"))
foodspinbox.place(x=300,y=245)
drinkspinbox = Spinbox(screen,from_=0,to=float("inf"))
drinkspinbox.place(x=300,y=345)
dessertspinbox = Spinbox(screen,from_=0,to=float("inf"))
dessertspinbox.place(x=300,y=445)

#progressbar

progressbar = Progressbar(screen,orient=HORIZONTAL,length = 200,mode='determinate')
progressbar.place(x=250,y=530)

#buttons
submit = Button(screen,text = "submit",command=both)
submit.place(x=310,y=500)

screen.mainloop()
