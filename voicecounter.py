import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import speech_recognition as sr
import random

screen = tk.Tk()
screen.title("voice counter")
screen.geometry("600x500")
screen.config(bg="black")

textt = ""
num = 0

#functions
def reset():
    num = 0
    numlab.config(text=str(num))

def trans():
    global textt
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        screen.update()
        audio = recog.listen(source)
        print("start speaking...")
        try:
            textt = recog.recognize_google(audio).lower()
            print(textt)
            return textt
            #if textt != "up" or textt != "add" or textt != "down" or textt != "minus":
             #   messagebox.showerror("error","command not recognised")
        except:
           messagebox.showerror("error","command not recognised")
           return ""
        
#== "up" or t == "add":
#== "down" or t == "minus"

def work():
    global textt
    global num
    t = trans()
    if t in ["up","add"]:
        num += 1
    elif t in ["down","minus"]:
        num -= 1
    else:
        messagebox.showerror("error","command not recognised")
    numlab.config(text=str(num))
    
#design
numlab = tk.Label(screen,text="0",font=("calibri",100,"bold"),fg="white",bg="black")
numlab.place(x=260,y=80)
voibut = tk.Button(screen,text="give command",bg="white",fg="black",font=("calibri",13),command=work)
voibut.place(x=170,y=300)
resbut = tk.Button(screen,text="reset",fg="black",bg="white",font=("calibri",13),command=reset)
resbut.place(x=340,y=300)

screen.mainloop()
