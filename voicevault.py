import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import speech_recognition as sr

screen = tk.Tk()
screen.title("voice vault")
screen.geometry("600x500")
screen.config(bg="#1D093F")

#functions

def trans():
    global textt
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("start speaking...")
        audio = recog.listen(source)
        try:
            textt = recog.recognize_google(audio)
        except:
            print("voice not recognised")
        
def check():
    global textt
    trans()
    password = "piano"
    textt = textt.lower()
    if textt == password:
        stalab.config(text="STATUS: UNLOCKED",foreground="#00AE34")
        stalab.place(x=150,y=150)
        messagebox.showinfo("","access granted")
    else:
        messagebox.showerror("error","access denied")


#designing
stalab = tk.Label(screen,text="STATUS: LOCKED",bg="#1D093F",foreground="#FF0000",font=("Agency FB",40))
stalab.place(x=170,y=150)
spebut = tk.Button(screen,text="speak password",bg="#2C1258",foreground="white",font=("Agency FB",14),command=check)
spebut.place(x=250,y=320)



screen.mainloop()