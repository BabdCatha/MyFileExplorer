from tkinter import *
from random import *
import os
from PIL import Image, ImageTk

#lstDir=next(os.walk("G:/Explorateur_de_fichiers"))[1]
lstDir=os.listdir("G:\Explorateur_de_fichiers")
print(len(lstDir))
print(lstDir)

def commande1():
    print("LaTeX")
def commande2():
    print("blob")
def quitter():
    print("Quitter")
    win1.destroy()

win1=Tk()
win1.title("Explorateur de fichiers")
win1.state("zoomed")

scrollbar1=Scrollbar(win1,orient=VERTICAL)
scrollbar1.pack(side=RIGHT,fill=Y)

menu1=Menu(win1)
filemenu = Menu(menu1, tearoff=0)
filemenu.add_command(label="LaTeX", command=commande1)
filemenu.add_command(label="Bouton très (in)utile", command=commande2)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitter)
menu1.add_cascade(label="Menuuuuu", menu=filemenu)
win1.config(menu=menu1)

x,y=win1.winfo_screenwidth(),win1.winfo_screenheight()-45
print(x,y)

can1=Canvas(width=x,height=y,highlightthickness=0)
can1.pack()

scrollbar1.config(command=can1.yview)

places=can1.create_rectangle(0,0,x/6,y/5*4,fill="grey")
files=can1.create_rectangle(x/6,0,x-18,y,fill="black")
notes=can1.create_rectangle(0,y/5*4,x/6,y,fill="white")

x1=x-18-95
x2=x/6+20
y1=y/5-95
y2=0+20

icon0=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/directory.png"))
icon0_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/directory_hidden.png"))
icon1=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/empty.png"))
icon1_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/empty_hidden.png"))
icon2=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/unknown.png"))
icon2_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/unknown_hidden.png"))
icon3=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/text.png"))
icon3_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/text_hidden.png"))
icon4=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/executable.png"))
icon4_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/executable_hidden.png"))
icon5=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/compressed.png"))
icon5_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/compressed_hidden.png"))
icon6=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/picture.png"))
icon6_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/picture_hidden.png"))
icon7=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/music.png"))
icon7_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/music_hidden.png"))
icon8=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/video.png"))
icon8_hid=ImageTk.PhotoImage(Image.open("G:/Explorateur_de_fichiers/images/video_hidden.png"))

for i in lstDir:
    lstLetters=[]
    for j in i:
        lstLetters.append(j)
    print(lstLetters)
    extFile=os.path.splitext(i)[1]
    print(extFile)
    if x2<x1:
        if lstLetters[0]==".":
            hidden=1
        else:
            hidden=0
        if extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==0:
            can1.create_image(x2+37.5,y2+37.5, image=icon6)
        elif extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==1:
            can1.create_image(x2+37.5,y2+37.5, image=icon6_hid)
        elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==0:
            can1.create_image(x2+37.5,y2+37.5, image=icon4)
        elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==1:
            can1.create_image(x2+37.5,y2+37.5, image=icon4_hid)
        else:
            if os.path.isfile(i)==True and hidden==0:
                print("file not hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon2)
            elif os.path.isfile(i)==True and hidden==1:
                print("file hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon2_hid)
            elif os.path.isfile(i)==False and hidden==0:
                print("dir not hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon0)
            elif os.path.isfile(i)==False and hidden==1:
                print("dir hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon0_hid)
        x2+=95
    else:
        x2,y2=x/6+20,y2+145
        if lstLetters[0]==".":
            hidden=1
        else:
            hidden=0
        if extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==0:
            can1.create_image(x2+37.5,y2+37.5, image=icon6)
        elif extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==1:
            can1.create_image(x2+37.5,y2+37.5, image=icon6_hid)
        elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==0:
            can1.create_image(x2+37.5,y2+37.5, image=icon4)
        elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==1:
            can1.create_image(x2+37.5,y2+37.5, image=icon4_hid)
        else:
            if os.path.isfile(i)==True and hidden==0:
                print("file not hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon2)
            elif os.path.isfile(i)==True and hidden==1:
                print("file hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon2_hid)
            elif os.path.isfile(i)==False and hidden==0:
                print("dir not hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon0)
            elif os.path.isfile(i)==False and hidden==1:
                print("dir hidden :",i)
                can1.create_image(x2+37.5,y2+37.5, image=icon0_hid)
        x2+=95

win1.mainloop()