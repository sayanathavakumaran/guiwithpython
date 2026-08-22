from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("700x500")

toppingslist = ["cheese","olives","jalapenos","mushrooms","peppers","chicken"]
choice = {}

title = Label(screen,text="pizza order")
title.place(x=310,y=20)

prices = {
    "cheese": 2.00,
    "olives": 1.75,
    "jalapenos": 2.05,
    "mushrooms": 2.25,
    "peppers": 0.95,
    "chicken": 2.10,
          }

sizes = {
    "small": 8.00,
    "medium": 10.00,
    "large": 12.00,
}

startx = 50
starty = 80
yspace = 40
for num, toppings in enumerate(toppingslist):
    var = IntVar()
    choice[toppings] = var
    Checkbutton(screen,text=toppings,variable=var).place(x=startx,y=starty+(yspace*num))

radiobuttonvals = StringVar()
radiosmall = Radiobutton(screen,text="small",variable = radiobuttonvals,value = "small")
radiosmall.place(x=200,y=80)
radiomed = Radiobutton(screen,text="medium",variable = radiobuttonvals,value = "medium")
radiomed.place(x=200,y=120)
radiolarge = Radiobutton(screen,text="large",variable = radiobuttonvals,value = "large")
radiolarge.place(x=200,y=160)

def total():
    global radiovals
    totalt = 0
    for toppings in toppingslist:
        if choice[toppings].get() == 1:
            totalt += prices[toppings]
    radiovals = radiobuttonvals.get()
    sizeprice = sizes[radiovals]
    total1 = totalt + sizeprice
    return total1


def display():
    total1 = total()
    listbox.insert(0,"size: "+radiovals)
    listbox.insert(1,"")
    listbox.insert(2,"toppings:")
    index = 3
    for num1, toppings in enumerate(choice):
        if choice[toppings].get()==1:
            listbox.insert(index+num1,toppings)
    listbox.insert(END,"")
    total2 = f"total: £{total1:.2f}"
    listbox.insert(END,total2)

subbutton = Button(screen,text="submit",command=display)
subbutton.place(x=110,y=350)

listbox = Listbox(screen,height=15,width=35)
listbox.place(x=400,y=70)
screen.mainloop()

