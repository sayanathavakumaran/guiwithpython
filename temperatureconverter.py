from tkinter import *

screen = Tk()
screen.geometry("500x400")
screen.config(background="mistyrose")

titlelabel = Label(screen,text="CELSIUS TO FAHRENHEIT",background="mistyrose",font=("calibri",17))
titlelabel.place(x=140,y=30)
questionlabel = Label(screen,text="enter the temperature in celsius: ",background="mistyrose",font=("calibri",11))
questionlabel.place(x=80,y=130)
entrybox = Entry(screen,text="",background="white",font=("calibri",11))
entrybox.place(x=300,y=130)
resultlabel = Label(screen,text="temperature in fahrenheit: ",background="mistyrose",font=("calibri",11))
resultlabel.place(x=80,y=200)
convertbutton = Button(screen,text="   convert   ",background="white")
convertbutton.place(x=210,y=285)


screen.mainloop()