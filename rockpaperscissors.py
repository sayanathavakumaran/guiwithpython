from tkinter import *

screen = Tk()
screen.geometry("700x350")
screen.config(background="maroon")
pscore = 0
cscore = 0

def compwin():
    global cscore, pscore
    cscore += 1
    winnerlabel.config(text="the computer wins !!")
    computerscorevallabel.config(text=str(cscore))
    playerscorevallabel.config(text=str(pscore))

def playwin():
    global cscore, pscore
    pscore += 1
    winnerlabel.config(text="the player wins !!")
    computerchosenvallabel.config(text=str(cscore))
    playerscorevallabel.config(text=str(pscore))

def tie():
    global cscore, pscore
    pscore += 1
    cscore += 1
    winnerlabel.config(text="it's a tie !!")
    computerchosenvallabel.config(text=str(cscore))
    playerscorevallabel.config(text=str(pscore))




titlelabel = Label(screen,text="rock paper scissors !!",background = "maroon",font=("calibri",18,"bold"),foreground="blanched almond")
titlelabel.place(x=245,y=20)
winnerlabel = Label(screen,text="----",background = "maroon",font=("calibri",14,"bold"),foreground="blanched almond")
winnerlabel.place(x=340,y=65)
youroptionlabel = Label(screen,text="your option:",background="maroon",font=("calibri",14,"bold"),foreground="blanched almond")
youroptionlabel.place(x=40,y=130)
rockbutton = Button(screen,text="rock",background="blanched almond",font=("calibri",11,"bold"),foreground="maroon")
rockbutton.place(x=240,y=135)
paperbutton = Button(screen,text="paper",background="blanched almond",font=("calibri",11,"bold"),foreground="maroon")
paperbutton.place(x=335,y=135)
scissorbutton = Button(screen,text="scissor",background="blanched almond",font=("calibri",11,"bold"),foreground="maroon")
scissorbutton.place(x=450,y=135)
scorelabel = Label(screen,text="score:",background="maroon",font=("calibri",14,"bold"),foreground="blanched almond")
scorelabel.place(x=89,y=220)
yourchosenvallabel = Label(screen,text="----",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
yourchosenvallabel.place(x=280,y=220)
yourchosenlabel = Label(screen,text="your chosen:",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
yourchosenlabel.place(x=180,y=220)
computerchosenvallabel = Label(screen,text="----",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
computerchosenvallabel.place(x=330,y=270)
computerchosenlabel = Label(screen,text="computer's chosen:",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
computerchosenlabel.place(x=180,y=270)
playerscorevallabel = Label(screen,text="----",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
playerscorevallabel.place(x=540,y=220)
playerscorelabel = Label(screen,text="player's score:",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
playerscorelabel.place(x=420,y=220)
computerscorevallabel = Label(screen,text="----",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
computerscorevallabel.place(x=560,y=270)
computerscorelabel = Label(screen,text="computer's score:",background="maroon",font=("calibri",13,"bold"),foreground="blanched almond")
computerscorelabel.place(x=420,y=270)


screen.mainloop()
