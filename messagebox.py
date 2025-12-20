from tkinter import *
from tkinter import messagebox
screen = Tk()
screen.geometry("600x500")
screen.config(background="light yellow")

label = Label(screen,text="**********",background="light yellow",font=("calibri",14,"bold"),foreground="maroon")
label.place(x=250,y=220)

#show info
messagebox.showinfo("window","no")

#show warning
messagebox.showwarning("window","danger")

#show error
messagebox.showerror("window","error")

#ask question
messagebox.askquestion("window","noodles?")

#cancel
messagebox.askokcancel("window","do you want to cancel?")

#ask yes or no
messagebox.askyesno("window","do you want pizza?")

#ask retry/cancel
messagebox.askretrycancel("window","retry or cancel?")


#ask yes, no or cancel
messagebox.askyesnocancel("window","yes, no or cancel?")

screen.mainloop()