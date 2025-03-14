#coding : UTF-8

import string
from random import randint , choice
from tkinter import *


def generation_nombre () :
    nombre_min = 1
    nomnbre_max = 1
    all_char = string.digits

    generation = "".join(choice(all_char) for x in range (randint(nombre_min , nomnbre_max)))
    text.delete(0 , END)
    text.insert(0 , generation)




window = Tk ()
window.title ("CHANCE-GO")
window.geometry ("1080x720")
window.iconbitmap("des.ico")
window.minsize (720 , 320)
window.config (background="#BFBFBF")

frame = Frame(window , bd = 1 , relief=SUNKEN , bg ="#8AA6A3")

width = 580
height = 400
image = PhotoImage(file="Dess.png").zoom(10).subsample(10)
canvas = Canvas (frame , width=width , height=height , bd = 0 , highlightthickness=0 , bg = "#BFBFBF")
canvas.create_image ( width/2 , height/2 , image=image)
canvas.pack()


text = Entry( frame , fg = "black" , font=("courrier" , 40) , bg ="#4C5958")
text.pack()

btn = Button(frame ,text="Lancer les Des" , fg = "black" , font=("courrier" , 35) , bg ="#4C5958" , command= generation_nombre)
btn.pack(fill=X)


frame.pack(expand=YES)


window.mainloop()