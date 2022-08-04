from tkinter import *
from turtle import st, width
#follow FinoanaRandria on Git Hub
window =Tk()
window.title("Generateur de mot de passe")

window.geometry("720x480")

window.config(background="Orange")

#partie Frame (Boite)

frame= Frame(window,bg="orange")

#ajouter une image ---Follow Finoana Randria On Git Hub-- 

width = 300
heigth = 300

image = PhotoImage(file="/home/finoana/Documents/Porjects Python Password/kaneki.png").zoom(35) .subsample(32)

canvas = Canvas(frame , width=width ,height=heigth , bg ="orange",bd=0,highlightthickness=0)

canvas.create_image(width/2 , heigth/2, image=image)

canvas.grid(row=0, column=0,sticky=W)

#ajouter une titre
titre = Label(frame,text="Mot de passe",font=("Helvetica",30), bg="orange",fg="white")
titre.grid(row=0,column=1,sticky=W)

frame.pack(expand=YES)

#champ 

window.mainloop()
