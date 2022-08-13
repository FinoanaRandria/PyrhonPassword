from random import randint,choice
from tkinter import *
from turtle import st, width

import string
#function

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password= "".join(choice(all_chars) for x in range (randint(password_min,password_max)))
    password_entry.delete(0 ,END)
    password_entry.insert(0, password)    
         
#follow FinoanaRandria on Git Hub
window =Tk()
window.title("Generateur de mot de passe")

window.geometry("820x580")
window.minsize(820,580)
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
#right frame

rigth_frame=Frame(frame,bg="orange")

#ajouter une titre
titre = Label(rigth_frame,text="Mot de passe",font=("Helvetica",30), bg="orange",fg="white")
titre.pack()

#Champ
password_entry = Entry(rigth_frame,font=("Helvetica",30), bg="orange",fg="black")
password_entry.pack()

#boutton 
boutton = Button(rigth_frame,text="Generer",font=("Helvetica",30), bg="orange",fg="white",command=generate_password)
boutton.pack(fill=X)

#replacement de la frame
rigth_frame.grid(row=0,column=1,sticky=W)


#pour affichier la Frame
frame.pack(expand=YES)


window.mainloop()
