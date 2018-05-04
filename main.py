from tkinter import *
from random import *
from platform import system
import subprocess
import os
from PIL import Image, ImageTk

#TODO: Make the window able to resize itself
#TODO: Backward/forward/reload buttons
#TODO: Fix file to launch/directory to open when clicking on an item after scrolling
#TODO: Fix bad files/directories order
#TODO: Fix scrolling zone issues
#TODO: Right-clic menu

system=system()
if system=="Windows":
    CurrentDir="C:/Windows"
else:
    CurrentDir="/home/babd_catha"
    
def commande1():
    print("LaTeX")
def commande2():
    print("blob")
def quitter():
    print("Quitter")
    win1.destroy()
    
def GetFileName(event):
    global numerocolonne,numeroligne,usedWidth,Grid,CurrentDir,DirGrid
    print(event.x)
    print(event.y)
    event.x-=usedWidth/6-3
    X=int(event.x//95)
    Y=event.y//145
    print(X,Y)
    nomfichier=Grid[X][Y]
    estUnDossier=DirGrid[X][Y]
    ouvrirfichier(CurrentDir + "/" + nomfichier, estUnDossier)

def ouvrirfichier(nomfichier,isDossier):
    global CurrentDir,OldDir
    if isDossier:
        OldDir=CurrentDir
        CurrentDir = nomfichier
        afficherDossier(nomfichier)
    elif system != "Windows":
        subprocess.call(["xdg-open", nomfichier])
    elif system == "Windows":
        os.startfile(nomfichier)

#def RightClicMenu():

win1=Tk()
win1.title("Explorateur de fichiers")
#win1.wm_client("Test")
favicon=ImageTk.PhotoImage(Image.open("images/favicon2_75.png"))
win1.tk.call('wm','iconphoto',win1._w,favicon)
#win1.state("zoomed") #For Windows only

scrollbar1=Scrollbar(win1,orient=VERTICAL)
scrollbar1.pack(side=RIGHT,fill=Y)
scrollbar2=Scrollbar(win1,orient=HORIZONTAL)
scrollbar2.pack(side=BOTTOM,fill=X)

menu1=Menu(win1)
filemenu = Menu(menu1, tearoff=0)
filemenu.add_command(label="LaTeX", command=commande1)
filemenu.add_command(label="Useless button", command=commande2)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitter)
menu1.add_cascade(label="Menu", menu=filemenu)
win1.config(menu=menu1)

realWidth,realHeight=win1.winfo_screenwidth(),win1.winfo_screenheight()
print(realWidth,realHeight)
usedWidth,usedHeight=realWidth-13,realHeight-1/20*realHeight
print(usedWidth,usedHeight)

can1=Canvas(width=usedWidth,height=usedHeight,highlightthickness=0,scrollregion=(0,0,usedWidth,usedHeight*3),bg="black")
can1.pack()
can1.bind("<Double-Button-1>",GetFileName)
can1.bind("<Button-3>",GetFileName)
can2=Canvas(width=usedWidth/6,heigh=usedHeight/5*4,highlightthickness=0,bg="grey")
can2.place(x=0,y=usedHeight/20)
can3=Canvas(width=usedWidth/6-3,heigh=usedHeight/20,highlightthickness=0,bg="gray8")
can3.place(x=0,y=0)

icon_reload=ImageTk.PhotoImage(Image.open("images/arrow-reload.png"))
icon_backward=ImageTk.PhotoImage(Image.open("images/arrow-backward.png"))
icon_forward=ImageTk.PhotoImage(Image.open("images/arrow-forward.png"))
#TODO: Fix buttons sizes, set actions
but1=Button(can3,image=icon_reload,width=75,height=48,bd=0,bg="black",activebackground="gray33")
but1.place(x=0,y=0)
but2=Button(can3,image=icon_backward,width=75,height=48,bd=0,bg="black",activebackground="gray33")
but2.place(x=(usedWidth/6-3)/100*38,y=0)
but3=Button(can3,image=icon_forward,width=75,height=48,bd=0,bg="black",activebackground="gray33")
but3.place(x=(usedWidth/6-3)/8*6,y=0)

scrollbar1.config(command=can1.yview)
can1['yscrollcommand']=scrollbar1.set
scrollbar2.config(command=can1.xview)
can1['xscrollcommand']=scrollbar2.set

"""testEntry=Text(win1,height=10,width=29)
testEntry.place(x=1,y=usedHeight/5*4+1)""" #TODO: BWAAAAAAAAAAAAAAH !!!
tempcan=Canvas(width=usedWidth/6,height=usedHeight/5,highlightthickness=0,bg="orange")
tempcan.place(x=0,y=usedHeight/5*4)
labelRouge=Label(bg="orange",fg="red",text="DANGER, ZONE EN TRAVAUX !")
labelRouge.place(x=usedWidth/35,y=usedHeight/5*4+0.44*usedHeight/5)

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
icon9=ImageTk.PhotoImage(Image.open("images/disc-image.png"))
icon9_hid=ImageTk.PhotoImage(Image.open("images/disc-image_hidden.png"))
icon10=ImageTk.PhotoImage(Image.open("images/apk.png"))
icon10_hid=ImageTk.PhotoImage(Image.open("images/apk_hidden.png"))
icon11=ImageTk.PhotoImage(Image.open("images/internet-file.png"))
icon11_hid=ImageTk.PhotoImage(Image.open("images/internet-file_hidden.png"))

def afficherDossier(dossier):
    
    global usedWidth,currentWidthIconPlacement,currentHeightIconPlacement,numeroligne,numerocolonne,Grid,DirGrid,can1,CurrentDir
    
    Grid=[] #grille qui contient les icones
    DirGrid=[] #pour différencier les fichiers qu'on peut ouvrir des dossiers à afficher
    numeroligne=0
    numerocolonne=0
    OldDir=""
    
    maxWidthIconPlacement=usedWidth-95 #add -18 after -95 if -13 is not present when usedWidth is defined
    currentWidthIconPlacement=usedWidth/6+20
    y1=usedHeight/5-95
    currentHeightIconPlacement=0+20

    #can1.create_rectangle(0,0,usedWidth,usedHeight,fill="Black") #Useless ?
    lstDir=os.listdir(dossier)
    def sortFilesDir():
        convert=lambda text: int(text) if text.isdigit() else text
        alphanum_key=lambda key: [convert(c) for c in re.split('([0-9]+)',key)]
        lstDir.sort(key=alphanum_key)
    sortFilesDir()

    for i in lstDir:
        lstLetters=[]
        for j in i:
            lstLetters.append(j)
        print(lstLetters)
        extFile=os.path.splitext(i)[1]
        print(extFile)

        if currentWidthIconPlacement>maxWidthIconPlacement:
            currentWidthIconPlacement,currentHeightIconPlacement=usedWidth/6+20,currentHeightIconPlacement+145
            numeroligne+=1
            numerocolonne = 0
        if currentWidthIconPlacement<maxWidthIconPlacement:
            hidden=1 if lstLetters[0]=="." else 0

            if numeroligne==0:
                Grid.append([])
                DirGrid.append([])
            
            if extFile==".txt" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon3)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".txt" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon3_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon4)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon4_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".zip" or extFile==".rar" or extFile==".7z" or extFile==".gz" or extFile==".xz" or extFile==".tar" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon5)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".zip" or extFile==".rar" or extFile==".7z" or extFile==".gz" or extFile==".xz" or extFile==".tar" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon5_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon6)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon6_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp3" or extFile==".m4a" or extFile==".wav" or extFile==".ogg" or extFile==".amr" or extFile==".flac" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon7)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp3" or extFile==".m4a" or extFile==".wav" or extFile==".ogg" or extFile==".amr" or extFile==".flac" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon7_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp4" or extFile==".avi" or extFile==".mkv" or extFile==".webm" or extFile==".flv" or extFile==".mov" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon8)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp4" or extFile==".avi" or extFile==".mkv" or extFile==".webm" or extFile==".flv" or extFile==".mov" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon8_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".iso" or extFile==".img" or extFile==".adf" or extFile==".bin" or extFile==".ima" or extFile==".image" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon9)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".iso" or extFile==".img" or extFile==".adf" or extFile==".bin" or extFile==".ima" or extFile==".image" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon_hid9)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".apk" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon10)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".apk" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon10_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".html" or extFile==".htm" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon11)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".html" or extFile==".htm" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon11_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            else:
                if os.path.isfile(os.path.join(CurrentDir,i))==False and hidden==0:
                    print("dir not hidden :",i)
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon0)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory=True
                elif os.path.isfile(os.path.join(CurrentDir,i))==False and hidden==1:
                    print("dir hidden :",i)
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon0_hid)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory=True
                elif hidden==0:
                        icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon1)
                        lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                        IsDirectory=False
                elif hidden==1:
                        icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon1_hid)
                        lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                        IsDirectory=False
                elif os.path.isfile(os.path.join(CurrentDir,i))==True and not extFile=="" and hidden==0:
                    print("file not hidden :",i)
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon2)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory=False
                elif os.path.isfile(os.path.join(CurrentDir,i))==True and not extFile=="" and hidden==1:
                    print("file hidden :",i)
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5, image=icon2_hid)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i,fill="white",width=75,justify=CENTER)
                    IsDirectory=False

            currentWidthIconPlacement+=95

            Grid[numerocolonne].append(i)
            DirGrid[numerocolonne].append(IsDirectory)
            numerocolonne+=1

afficherDossier(CurrentDir)

win1.mainloop()

#https://github.com/BabdCatha/MyFileExplorer
