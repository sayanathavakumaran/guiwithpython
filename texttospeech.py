'''LanguageﾠCode
Englishﾠen
Hindiﾠhi
Frenchﾠfr
Spanishﾠes
Germanﾠde
Japaneseﾠja
Tamilﾠta
Teluguﾠte'''

from tkinter import *
from gtts import gTTS
import os

screen = Tk()
screen.geometry("500x500")

def convert():
    language = "ta"
    textt = entry.get()
    translater = gTTS(text=textt,lang=language,slow=False)
    translater.save("speech.wav")
    os.system("speech.wav")


frame1 = Frame(screen,bg = "#FFEDF6",height=150)
frame1.pack(fill=X)
frame2 = Frame(screen,bg = "#1B1B3E",height=350)
frame2.pack(fill=X)
label = Label(frame1,text="text to speech converter",font=("times new roman",20),bg = "#FFEDF6")
label.place(x=120,y=50)
entry = Entry(frame2,width=30,font=("times new roman",14))
entry.place(x=110,y=75)
button = Button(frame2,text="submit",bg="#FFEDF6",font=("times new roman",14),command=convert)
button.place(x=210,y=180)

screen.mainloop()