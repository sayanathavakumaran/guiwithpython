import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import speech_recognition as sr

screen = tk.Tk()
screen.title("speech to text converter")
screen.geometry("600x300")
screen.config(bg="light grey")

#functions
def trans():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        textbox.delete(1.0,tk.END)
        print("start speaking...")
        audio = recog.listen(source)
        try:
            textt = recog.recognize_google(audio)
        except:
            textt = "voice not recognised"
        textbox.delete(1.0,tk.END)
        textbox.insert(tk.END,textt)
    
def save():
    fileext = filedialog.asksaveasfile(defaultextension=".txt")
    if fileext:
        fileext.write(textbox.get(1.0,tk.END))
        fileext.close()
    else:
        messagebox.showerror("error","try again")



#design
titlelabel = tk.Label(screen,text="voice notepad",bg="light grey", font=("times new roman",17))
titlelabel.place(x=235,y=40)
clickbutton = tk.Button(screen,text="click to start recording",font=("times new roman",11),command=trans)
clickbutton.place(x=30,y=140)
textbox = tk.Text(screen,height=7,width=26)
textbox.place(x=200,y=140)
savebutton = tk.Button(screen,text="save as a file",font=("times new roman",11),command=save)
savebutton.place(x=450,y=140)
#speaklabel = tk.Label(screen,bg="white", font=("times new roman",17))
#speaklabel.place(x=230,y=145)


screen.mainloop()