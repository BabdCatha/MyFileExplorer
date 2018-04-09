from tkinter import *
from random import *
from platform import system
import os
from PIL import Image, ImageTk

#TODO: Make the window able to resize itself

#lstDir=next(os.walk("/media/tardis/F8C7-7F8C/Explorateur_de_fichiers"))[1]
system = system()
if system == "Windows":
    lstDir=os.listdir("C:\Windows")
else:
    lstDir=os.listdir("/home/babd_catha")
    
print(len(lstDir))
print(lstDir)

def commande1():
    print("LaTeX")
def commande2():
    print("blob")
def quitter():
    print("Quitter")
    win1.destroy()
    
def GetFileName(event):
    global numerocolonne, numeroligne
    print(event.x)
    print(event.y)
    
    
def ouvrirfichier(nomfichier):
    print(nomfichier) #Faut que je finisse GetFile avant de finir ça

win1=Tk()
win1.title("Explorateur de fichiers")
#win1.state("zoomed")

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

can1=Canvas(width=x,height=y,highlightthickness=0,scrollregion=(0,0,x,y*1.5),bg="black")
can1.pack()
can1.bind("<Double-Button-1>", GetFileName)
can2=Canvas(width=x/6-3,heigh=y/5*4,highlightthickness=0,bg="grey") #-3 : alignement avec le bloc notes (/!\ qui ne marche pas)
can2.place(x=0,y=0)

scrollbar1.config(command=can1.yview)

#places=can1.create_rectangle(0,0,x/6,y/5*4,fill="grey")
#files=can1.create_rectangle(x/6,0,x-18,y,fill="black")
#notes=can1.create_rectangle(0,y/5*4,x/6,y,fill="white")

testEntry=Text(win1,height=10,width=29)
testEntry.place(x=1,y=y/5*4+1)

x1=x-18-95 #C'est pareil, vous auriez pu faire x_max, x_icon ou des trucs comme ça :)
x2=x/6+20
y1=y/5-95
y2=0+20

#Celui qui a eu l'idée d'appeller les icones icon1, icon2 etc... est un débile, c'est pas pratique du tout :p
#Faut toujours utiliser de chemins relatifs quand on sais pas ou le fichier va s'executer
icon0=ImageTk.PhotoImage(Image.open("images/directory.png"))
icon0_hid=ImageTk.PhotoImage(Image.open("images/directory_hidden.png"))
icon1=ImageTk.PhotoImage(Image.open("images/empty.png"))
icon1_hid=ImageTk.PhotoImage(Image.open("images/empty_hidden.png"))
icon2=ImageTk.PhotoImage(Image.open("images/unknown.png"))
icon2_hid=ImageTk.PhotoImage(Image.open("images/unknown_hidden.png"))
icon3=ImageTk.PhotoImage(Image.open("images/text.png"))
icon3_hid=ImageTk.PhotoImage(Image.open("images/text_hidden.png"))
icon4=ImageTk.PhotoImage(Image.open("images/executable.png"))
icon4_hid=ImageTk.PhotoImage(Image.open("images/executable_hidden.png"))
icon5=ImageTk.PhotoImage(Image.open("images/compressed.png"))
icon5_hid=ImageTk.PhotoImage(Image.open("images/compressed_hidden.png"))
icon6=ImageTk.PhotoImage(Image.open("images/picture.png"))
icon6_hid=ImageTk.PhotoImage(Image.open("images/picture_hidden.png"))
icon7=ImageTk.PhotoImage(Image.open("images/music.png"))
icon7_hid=ImageTk.PhotoImage(Image.open("images/music_hidden.png"))
icon8=ImageTk.PhotoImage(Image.open("images/video.png"))
icon8_hid=ImageTk.PhotoImage(Image.open("images/video_hidden.png"))

Grid = [] #grille qui contient les icones
DirGrid = [] #pour différencier les fichiers qu'on peut ouvrir des dossiers à afficher
numeroligne = 0
numerocolonne = 0
#IsDirectory = False

def afficherDossier():
    
    global x,x2,y2,numeroligne,numerocolonne,Grid,Dirgrid,can1

    for i in lstDir:
        lstLetters=[]
        for j in i:
            lstLetters.append(j)
        print(lstLetters)
        extFile=os.path.splitext(i)[1]
        print(extFile)
        if x2>x1:
            x2,y2=x/6+20,y2+145
            numeroligne+=1
            numerocolonne = 0
        if x2<x1:
            hidden = 1 if lstLetters[0]=="." else 0
            
            if numeroligne == 0:
                Grid.append([])
                DirGrid.append([])
            
            if extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==0:
                icon = can1.create_image(x2+37.5,y2+37.5, image=icon6)
                lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory = False
            elif extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==1:
                icon = can1.create_image(x2+37.5,y2+37.5, image=icon6_hid)
                lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory = False
            elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==0:
                icon = can1.create_image(x2+37.5,y2+37.5, image=icon4)
                lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory = False
            elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==1:
                icon = can1.create_image(x2+37.5,y2+37.5, image=icon4_hid)
                lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory = False
            else:
                if os.path.isfile(i)==True and hidden==0:
                    print("file not hidden :",i)
                    icon = can1.create_image(x2+37.5,y2+37.5, image=icon2)
                    lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory = False
                elif os.path.isfile(i)==True and hidden==1:
                    print("file hidden :",i)
                    icon = can1.create_image(x2+37.5,y2+37.5, image=icon2_hid)
                    lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory = False
                elif os.path.isfile(i)==False and hidden==0:
                    print("dir not hidden :",i)
                    icon = can1.create_image(x2+37.5,y2+37.5, image=icon0)
                    lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory = True
                elif os.path.isfile(i)==False and hidden==1:
                    print("dir hidden :",i)
                    icon = can1.create_image(x2+37.5,y2+37.5, image=icon0_hid)
                    lab1=can1.create_text(x2+37.5,y2+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory = True
            x2+=95
            
            Grid[numerocolonne].append(i)
            DirGrid[numerocolonne].append(IsDirectory)
            numerocolonne+=1
            
afficherDossier()

win1.mainloop()

#Double clic : <Double-Button-1>
#https://github.com/BabdCatha/MyFileExplorer
