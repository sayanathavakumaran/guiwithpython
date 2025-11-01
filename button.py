from tkinter import *

#creating the base
screen = Tk()

screen.config(background = "midnightblue")
#resizing the base
screen.geometry("400x400")

#function
def editlabel():
    usertext = entrybox.get()
    label2.config(text = usertext)


#creating the widget
button = Button(screen,text="click here",background = "cadetblue",foreground = "powderblue",command = screen.destroy)

#positioning the widget
button.place(x=170,y=185)

label = Label(screen,text="click button below to close screen",background = "midnightblue",foreground = "lightblue",font = ("Verdana",12))
label.place(x = 64,y=100)

entrybox = Entry(screen,background = "lavender",foreground = "lavender",font = ("Verdana",12))
entrybox.place(x = 100,y = 250)

button2 = Button(screen,text = "submit",background = "palevioletred",foreground = "mistyrose",font = ("verdana",9),command = editlabel)
button2.place(x = 175,y = 300)


label2 = Label(screen,background = "midnightblue",foreground = "lightblue",font = ("Verdana",14))
label2.place(x = 180,y = 50)

#holding the output
screen.mainloop()