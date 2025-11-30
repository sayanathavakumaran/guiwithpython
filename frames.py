from tkinter import *

screen=Tk()
screen.geometry("400x400")
screen.config(background="seashell")

icecreamlabel = Label(screen,text="ICE CREAMS",background="seashell",font=(20),foreground="black")
icecreamlabel.pack()

#creating frame

horiframe = Frame(screen)
horiframe.pack(pady=20)
chocobutton = Button(horiframe,text="chocolate",background="sienna",foreground = "white")
chocobutton.pack(side=LEFT)
bananabutton = Button(horiframe,text="banana",background="lemonchiffon",foreground="peru")
bananabutton.pack(side=LEFT)
mintbutton = Button(horiframe,text="mintchip",background="mediumspringgreen",foreground="saddlebrown")
mintbutton.pack(side=LEFT)

vertiframe = Frame(screen)
vertiframe.pack(side=BOTTOM,pady=(0,120))
cookiedoughbutton = Button(vertiframe,text="cookie dough",background="lemonchiffon",foreground="saddlebrown")
cookiedoughbutton.pack(side=BOTTOM)
marshmallowbutton = Button(vertiframe,text="marshmallow",background="pink",foreground="white")
marshmallowbutton.pack(side=BOTTOM)
caramelsaucebutton = Button(vertiframe,text="caramel drizzle",background="peru",foreground="blanchedalmond")
caramelsaucebutton.pack(side=BOTTOM)
chocolatesaucebutton = Button(vertiframe,text="chocolate drizzle",background="sienna",foreground="white")
chocolatesaucebutton.pack(side=BOTTOM)

screen.mainloop()
