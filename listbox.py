from tkinter import *

screen = Tk()
screen.geometry("400x500")
screen.config(background="maroon")


titlelabel = Label(screen,text="flowers",background="maroon",font=("calibri",15,"bold"),fg="blanched almond")

listbox = Listbox(screen,height=10,bg="blanched almond",activestyle="dotbox",font="calibri",fg="maroon")
listbox.insert(1,"roses")
listbox.insert(2,"lotus")
listbox.insert(3,"tulip")
listbox.insert(4,"tigerlily")
listbox.insert(5,"marigold")
listbox.insert(6,"chrysanthemum")
listbox.insert(7,"lavender")
listbox.insert(8,"sunflower")
listbox.insert(9,"daffodil")
listbox.insert(10,"amaryllis")

titlelabel.pack(side=TOP,pady=(35,0))
listbox.pack(side=TOP,pady=(50,0))

screen.mainloop()