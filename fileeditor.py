from tkinter import *
from tkinter.filedialog import*

screen = Tk()
frame = Frame(screen)

#functions

def add():
    entry1 = entrybox.get()
    listbox.insert(END,entry1)
    entrybox.delete(0,END)

def delete():
    choice = listbox.curselection()
    listbox.delete(choice)

def open():
    dialogbox = askopenfile(title="open a file")
    if dialogbox is not None:
        listbox.delete(0,END)
        filecontents = dialogbox.readlines()
        for i in filecontents:
            listbox.insert(END,i.strip())

def save():
    dialogbox = asksaveasfile(defaultextension=".txt")
    if dialogbox is not None:
        for i in listbox.get(0,END):
            print(i.strip(),file=dialogbox)
            listbox.delete(0,END)

openbutton = Button(screen,text="open",command=open)
savebutton = Button(screen,text="save",command=save)
addbutton = Button(screen,text="add",command=add)
deletebutton = Button(screen,text="delete",command=delete)
entrybox = Entry(screen)
openbutton.pack(side=LEFT,padx=(20,15),pady=(10,10))
deletebutton.pack(side=RIGHT,padx=(15,20),pady=(10,10))
savebutton.pack(padx=(10,10),pady=(20,15))
entrybox.pack(padx=(20,20),pady=(20,20))
addbutton.pack(padx=(10,10),pady=(15,20))
scrollbar = Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(frame,width=75,yscrollcommand=scrollbar.set)
for x in range(100001):
    listbox.insert(END,"list"+str(x))
listbox.pack(side=LEFT)
scrollbar.config(command=listbox.yview)
frame.pack(side=RIGHT,pady=(0,20))
screen.mainloop()
