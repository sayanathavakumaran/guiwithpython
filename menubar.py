from tkinter import *
from tkinter.ttk import *

screen = Tk()
screen.geometry("350x250")

screen.title("menu")
screen.config(background="light pink")
menubar = Menu(screen)

#adding menu options

settings = Menu(menubar,tearoff=0)
menubar.add_cascade(label="settings",menu=settings)
settings.add_command(label="profile",command=None)
settings.add_command(label="bluetooth",command=None)
settings.add_command(label="wifi",command=None)
settings.add_separator()
settings.add_command(label="background",command=None)
settings.add_command(label="apps",command=None)

file = Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=file)
file.add_command(label="new",command=None)
file.add_command(label="open",command=None)
file.add_command(label="save",command=None)
file.add_separator()
file.add_command(label="share",command=None)

edit = Menu(menubar,tearoff=0)
menubar.add_cascade(label="edit",menu=edit)
edit.add_command(label="undo",command=None)
edit.add_command(label="redo",command=None)
edit.add_separator()
edit.add_command(label="cut",command=None)
edit.add_command(label="copy",command=None)
edit.add_command(label="paste",command=None)

screen.config(menu=menubar)
screen.mainloop()



