from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("200x200")
screen.config(bg="paleturquoise")

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
    

progressbar = Progressbar(screen,orient=HORIZONTAL,length = 100,mode='determinate')
progressbar.place(x=50,y=40)
start = Button(screen,text="start",command=progressing)
start.place(x=60,y=80)

screen.mainloop()