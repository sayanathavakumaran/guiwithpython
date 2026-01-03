from tkinter import *
from tkinter.ttk import *
from time import strftime


screen = Tk()
screen.title("digital clock")

def time():
    timeformat = strftime('%H:%M:%S %p')
    clocklabel.config(text=timeformat)
    clocklabel.after(1000,time)

clocklabel = Label(screen,background="black",font=("ariel",50,"bold"),foreground="white")
clocklabel.pack(anchor="center")
time()

screen.mainloop()