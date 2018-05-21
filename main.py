from tkinter import *
from random import *
from platform import system
import subprocess
import os
from PIL import Image, ImageTk
import shutil
import hashlib

#TODO: Make the window able to resize itself
#TODO: Forward button
#TODO: Left panel items
#TODO: Fix opening file after going forward issue
#TODO: Add informations in Properties : file size (human readeable), type (xdg), location, ...
#TODO: Fix directories Properties

#FileNameclique="" #Not used
LastDir=""
NextDir=""
CopiedFile=""
RememberChoice=0 #In order to remember to delete automatically items

system=system()
if system=="Windows":
    CurrentDir="tests"
else:
    CurrentDir="/home/babd_catha"

LastDir=CurrentDir

def commande1():
    print("LaTeX")
def commande2():
    print("blob")
def quitter():
    print("Quitter")
    win1.destroy()

def GetFileName(event):
    global numerocolonne,numeroligne,usedWidth,Grid,CurrentDir,DirGrid
    ScrollbarPosition=scrollbar1.get()
    Z=ScrollbarPosition[0]
    Z=(usedHeight+320)*Z
    event.x-=usedWidth/6-3
    X=int(event.x//95)
    Y=int((event.y+Z)//130)
    print("\nDouble-left clic :\nx :",event.x,"\ny :",event.y,"\nRow :",X,"\nColumn :",Y,"\n") #Debug
    FileName=Grid[X][Y]
    estUnDossier=DirGrid[X][Y]
    OpenFile(CurrentDir+"/"+FileName,estUnDossier)

def OpenFile(FileName,isDossier):
    global CurrentDir,OldDir,LastDir
    if isDossier:
        LastDir=CurrentDir
        CurrentDir=FileName
        AfficherDossier(FileName)
    elif system!="Windows":
        subprocess.call(["xdg-open",FileName])#Do not open files correctly
        #subprocess.call(["mimeopen",FileName])#Close files when file explorer is closed
    elif system=="Windows":
        os.startfile(FileName)

win1=Tk()
win1.title("Explorateur de fichiers")
favicon=ImageTk.PhotoImage(Image.open("images/favicon2_75.png"))
win1.tk.call('wm','iconphoto',win1._w,favicon)
#win1.state("zoomed") #For Windows only

scrollbar1=Scrollbar(win1,orient=VERTICAL)
scrollbar1.pack(side=RIGHT,fill=Y)
scrollbar2=Scrollbar(win1,orient=HORIZONTAL)
scrollbar2.pack(side=BOTTOM,fill=X)

menu1=Menu(win1)
filemenu=Menu(menu1, tearoff=0)
filemenu.add_command(label="LaTeX",command=commande1)
filemenu.add_command(label="Useless button",command=commande2)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitter)
menu1.add_cascade(label="Menu",menu=filemenu)
win1.config(menu=menu1)

realWidth,realHeight=win1.winfo_screenwidth(),win1.winfo_screenheight()
usedWidth,usedHeight=realWidth-13,realHeight-1/20*realHeight
print("Screen resolution :\nReal x (realHeight) :",realHeight,"\nReal y (realWidth) :",realWidth,"\nUsed x (usedHeight) :",usedHeight,"\nUsed y (usedWidth) :",usedWidth,"\n") #Debug

can1=Canvas(width=usedWidth,height=usedHeight,highlightthickness=0,scrollregion=(0,0,usedWidth,usedHeight*1.5),bg="black")
can1.pack()
can1.bind("<Double-Button-1>",GetFileName)

def Reload():
    AfficherDossier(CurrentDir)

def GoBack():
    global LastDir,NextDir,CurrentDir
    NextDir=CurrentDir
    OpenFile(LastDir, True)

"""def GoForward():
    LastDir,NextDir,CurrentDir""" #TODO: JUST DO IT !!!
    
def CreateNewDirectory(a, WinNewDirectory):
    global CurrentDir #Must be an argument even if it is not used
    NewDirectoryName=str(a)
    MakeNewDirectory=CurrentDir+"/"+str(NewDirectoryName)
    if not os.path.exists(MakeNewDirectory):
        os.makedirs(MakeNewDirectory)
        Reload()
        WinNewDirectory.destroy()

def NewDir(CurrentDir):
    WinNewDirectory=Toplevel(win1)
    WinNewDirectory.configure(bg="black")
    WinNewDirectory.title("Nouveau dossier")
    NewDirLabel=Label(WinNewDirectory,bg="black",fg="white",text="Entrez ici le nom du dossier à créer :")
    NewDirLabel.pack()
    NewDirectoryName=StringVar(WinNewDirectory)
    NameDir=Entry(WinNewDirectory,bg="white",fg="black",textvariable=NewDirectoryName)
    NameDir.bind("<Return>",lambda x : CreateNewDirectory(NameDir.get(), WinNewDirectory))
    NameDir.pack(side=TOP)
    WinNewDirectory.mainloop()

def CopyFile(FileName):
    global CurrentDir,CopiedFile
    CopiedFile=os.path.join(CurrentDir,FileName)

def PasteFile(Directory):
    global CopiedFile
    if os.path.isfile(CopiedFile)==False:
        shutil.copytree(CopiedFile,Directory)
    elif os.path.isfile(CopiedFile)==True:
        shutil.copy2(CopiedFile,Directory)
    AfficherDossier(CurrentDir)

def Rename(CurrentDir,FileName):
    def RenameFile(a): #Must be an argument even if it is not used
        NewFileName=str(FileRename.get())
        NewFileName=CurrentDir+"/"+str(NewFileName)
        WinRename.destroy()
        shutil.move(str(CurrentDir)+"/"+str(FileName),str(NewFileName))
        Reload()
    WinRename=Toplevel(win1)
    WinRename.configure(bg="black")
    WinRename.title("Renommer un fichier")
    RenameLabel=Label(WinRename,bg="black",fg="white",text="Entrez ici le nouveau nom du fichier :")
    RenameLabel.pack()
    NewFileName=StringVar(WinRename)
    FileRename=Entry(WinRename,bg="white",fg="black",textvariable=NewFileName)
    FileRename.bind("<Return>",RenameFile)
    FileRename.pack(side=TOP)
    WinRename.mainloop()

def ConfirmDelete(CurrentDir,FileName): #For "Yes" button
    if os.path.isfile(os.path.join(CurrentDir,FileName))==True:
        os.remove(os.path.join(CurrentDir,FileName))
        AfficherDossier(CurrentDir)
    elif os.path.isfile(os.path.join(CurrentDir,FileName))==False:
        if os.listdir(os.path.join(CurrentDir,FileName))==[]:
            os.rmdir(os.path.join(CurrentDir,FileName))
            AfficherDossier(CurrentDir)
        elif os.listdir(os.path.join(CurrentDir,FileName))!=[]:
            shutil.rmtree(os.path.join(CurrentDir,FileName))
            AfficherDossier(CurrentDir)
    WinDeleteConfirm.destroy()
def CancelDelete():  #For "No" button
    WinDeleteConfirm.destroy()
def DeleteFile(FileName): #Main delete confirmation window
    global Grid,X,Y,DirGrid,CurrentDir,WinDeleteConfirm,RememberChoice
    """def OneToZeroAndZeroToOne():
        global RememberChoice
        if RememberChoice==0:
            RememberChoice=1
        elif RememberChoice==1:
            RememberChoice=0
    print("RememberChoice",RememberChoice)""" #Not working
    if 0==0: #Not working : RememberChoice==0
        WinDeleteConfirm=Toplevel(win1)
        WinDeleteConfirm.title("Supprimer un élément")
        WinDeleteConfirm.configure(bg="black")
        WarningLabel=Label(WinDeleteConfirm,bg="black",fg="white",text="Êtes vous sûr de vouloir supprimer\n\""+str(FileName)+"\" ?")
        WarningLabel.pack(side=TOP)
        RememberChoice=IntVar()
        RememberChoiceCheckbutton=Checkbutton(WinDeleteConfirm,bg="black",fg="grey50",highlightthickness=0,text="À l'avenir, ne plus demander et supprimer directement") #Not working, add : command=lambda:OneToZeroAndZeroToOne()
        RememberChoiceCheckbutton.pack(side=TOP)
        YesButton=Button(WinDeleteConfirm,bg="black",fg="white",highlightthickness=0,text="Oui",command=lambda:ConfirmDelete(CurrentDir,FileName))
        YesButton.pack(side=RIGHT)
        NoButton=Button(WinDeleteConfirm,bg="black",fg="white",highlightthickness=0,text="Non",command=CancelDelete)
        NoButton.pack(side=RIGHT)
        WinDeleteConfirm.mainloop()
    else:
        ConfirmDelete(CurrentDir,FileName) #Working ... Unfortunately ...

def Properties(FileName):
    global CurrentDir
    OctSize=os.path.getsize(str(CurrentDir)+"/"+str(FileName))
    MD5Hash=hashlib.md5(open(str(CurrentDir)+"/"+str(FileName),"rb").read()).hexdigest()
    SHA1Hash=hashlib.sha1(open(str(CurrentDir)+"/"+str(FileName),"rb").read()).hexdigest()
    SHA512Hash=hashlib.sha512(open(str(CurrentDir)+"/"+str(FileName),"rb").read()).hexdigest()
    WinProperties=Toplevel(win1)
    WinProperties.configure(bg="black")
    Label(WinProperties,bg="black",fg="white",justify=LEFT,text="Nom : "+str(FileName)+"\nTaille : "+str()+"("+str(OctSize)+" octets)").pack()
    #TODO: If not a directory, execute what follows
    Label(WinProperties,bg="black",fg="white",justify=LEFT,text="Sommes de contrôle :").pack()
    Label(WinProperties,bg="black",fg="white",justify=LEFT,text="MD5 :").pack()
    MD5Entry=Entry(WinProperties,bg="black",fg="white",highlightthickness=0)
    MD5Entry.insert(END,str(MD5Hash))
    MD5Entry.pack()
    Label(WinProperties,bg="black",fg="white",justify=LEFT,text="SHA1 :").pack()
    SHA1Entry=Entry(WinProperties,bg="black",fg="white",highlightthickness=0)
    SHA1Entry.insert(END,str(SHA1Hash))
    SHA1Entry.pack()
    Label(WinProperties,bg="black",fg="white",justify=LEFT,text="SHA512 :").pack()
    SHA512Entry=Entry(WinProperties,bg="black",fg="white",highlightthickness=0)
    SHA512Entry.insert(END,str(SHA512Hash))
    SHA512Entry.pack()

def sortFilesDir(lstDir):
    convert=lambda text:int(text) if text.isdigit() else text
    alphanum_key=lambda key:[convert(i) for i in re.split('([0-9]+)',key)]
    lstDir.sort(key=alphanum_key)

RightClic=Menu(win1,tearoff=0)
RightClic.add_command(label="Nouveau dossier",command=lambda:NewDir(CurrentDir))#TODO
RightClic.add_command(label="Copier",command=lambda:CopyFile(Grid[int(X)][int(Y)]))
RightClic.add_command(label="Coller",command=lambda:PasteFile(CurrentDir))
RightClic.add_command(label="Renommer",command=lambda:Rename(CurrentDir,Grid[int(X)][int(Y)]))
RightClic.add_command(label="Supprimer",command=lambda:DeleteFile(Grid[int(X)][int(Y)]))
RightClic.add_command(label="Propriétés",command=lambda:Properties(Grid[int(X)][int(Y)]))
def RightClicMenu(event):
    if event.x>=realWidth/6 and event.y>=0:
        try:
            RightClic.tk_popup(event.x_root+60,event.y_root+11,0)
            global numerocolonne,numeroligne,usedWidth,Grid,CurrentDir,DirGrid,X,Y
            try:
                event.x-=usedWidth/6-3
                X=int(event.x//95)
                Y=int(event.y//145)
                print("\nRight clic :\nx :",event.x,"\ny :",event.y,"\nRow :",X,"\nColumn :",Y,"\n") #Debug
                FileName=Grid[X][Y]
                estUnDossier=DirGrid[X][Y]
            except:
                pass
        finally:
            RightClic.grab_release()

win1.bind("<Button-3>",RightClicMenu)

can2=Canvas(width=usedWidth/6,heigh=usedHeight/5*4,highlightthickness=0,bg="grey")
can2.place(x=0,y=usedHeight/20)
can3=Canvas(width=usedWidth/6-3,heigh=usedHeight/20,highlightthickness=0,bg="gray8")
can3.place(x=0,y=0)

icon_reload=ImageTk.PhotoImage(Image.open("images/arrow-reload.png"))
icon_backward=ImageTk.PhotoImage(Image.open("images/arrow-backward.png"))
icon_forward=ImageTk.PhotoImage(Image.open("images/arrow-forward.png"))
#TODO: Fix buttons sizes
but1=Button(can3,image=icon_reload,width=75,height=48,bd=0,bg="black",activebackground="gray33",command=Reload)
but1.place(x=0,y=0)
but2=Button(can3,image=icon_backward,width=75,height=48,bd=0,bg="black",activebackground="gray33",command=GoBack)
but2.place(x=(usedWidth/6-3)/100*38,y=0)
but3=Button(can3,image=icon_forward,width=75,height=48,bd=0,bg="black",activebackground="gray33")
but3.place(x=(usedWidth/6-3)/8*6,y=0)

scrollbar1.config(command=can1.yview)
can1['yscrollcommand']=scrollbar1.set
scrollbar2.config(command=can1.xview)
can1['xscrollcommand']=scrollbar2.set

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

def AfficherDossier(dossier):

    global usedWidth,currentWidthIconPlacement,currentHeightIconPlacement,numeroligne,numerocolonne,Grid,DirGrid,can1,CurrentDir,LastDir

    Grid=[] #grille qui contient les icones
    DirGrid=[] #pour différencier les fichiers qu'on peut ouvrir des dossiers à afficher
    numeroligne=0
    numerocolonne=0

    maxWidthIconPlacement=usedWidth-95 #add -18 after -95 if -13 is not present when usedWidth is defined
    currentWidthIconPlacement=usedWidth/6+20
    y1=usedHeight/5-95
    currentHeightIconPlacement=0+20

    can1.create_rectangle(0,0,usedWidth,usedHeight,fill="Black")
    lstDir=os.listdir(dossier)
    sortFilesDir(lstDir)

    for i in lstDir:
        lstLetters=[]
        for j in i:
            lstLetters.append(j)
        #print(lstLetters) # For testing purposes
        extFile=os.path.splitext(i)[1]
        print(extFile)
        if len(i)>17:
            nameLength=len(i)-17
            i2=i[:-nameLength]
            i2=i2+"..."
        else:
            i2=i

        if currentWidthIconPlacement>maxWidthIconPlacement:
            currentWidthIconPlacement,currentHeightIconPlacement=usedWidth/6+20,currentHeightIconPlacement+145
            numeroligne+=1
            numerocolonne=0
        if currentWidthIconPlacement<maxWidthIconPlacement:
            hidden=1 if lstLetters[0]=="." else 0

            if numeroligne==0:
                Grid.append([])
                DirGrid.append([])

            if extFile==".txt" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon3)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".txt" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon3_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon4)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".exe" or extFile==".sh" or extFile==".com" or extFile==".bat" or extFile==".py" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon4_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".zip" or extFile==".rar" or extFile==".7z" or extFile==".gz" or extFile==".xz" or extFile==".tar" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon5)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".zip" or extFile==".rar" or extFile==".7z" or extFile==".gz" or extFile==".xz" or extFile==".tar" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon5_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon6)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".jpg" or extFile==".png" or extFile==".gif" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon6_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp3" or extFile==".m4a" or extFile==".wav" or extFile==".ogg" or extFile==".amr" or extFile==".flac" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon7)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp3" or extFile==".m4a" or extFile==".wav" or extFile==".ogg" or extFile==".amr" or extFile==".flac" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon7_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp4" or extFile==".avi" or extFile==".mkv" or extFile==".webm" or extFile==".flv" or extFile==".mov" or extFile==".vob" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon8)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".mp4" or extFile==".avi" or extFile==".mkv" or extFile==".webm" or extFile==".flv" or extFile==".mov" or extFile==".vob" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon8_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".iso" or extFile==".img" or extFile==".adf" or extFile==".bin" or extFile==".ima" or extFile==".image" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon9)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".iso" or extFile==".img" or extFile==".adf" or extFile==".bin" or extFile==".ima" or extFile==".image" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon_hid9)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".apk" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon10)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".apk" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon10_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".html" or extFile==".htm" and hidden==0:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon11)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            elif extFile==".html" or extFile==".htm" and hidden==1:
                icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon11_hid)
                lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                IsDirectory=False
            else:
                if os.path.isfile(os.path.join(CurrentDir,i))==False and hidden==0:
                    #print("dir not hidden :",i) # For testing purposes
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon0)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                    IsDirectory=True
                elif os.path.isfile(os.path.join(CurrentDir,i))==False and hidden==1:
                    #print("dir hidden :",i) # For testing purposes
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon0_hid)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                    IsDirectory=True
                elif hidden==0:
                        icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon1)
                        lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                        IsDirectory=False
                elif hidden==1:
                        icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon1_hid)
                        lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                        IsDirectory=False
                elif os.path.isfile(os.path.join(CurrentDir,i))==True and not extFile=="" and hidden==0:
                    #print("file not hidden :",i) # For testing purposes
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon2)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                    IsDirectory=False
                elif os.path.isfile(os.path.join(CurrentDir,i))==True and not extFile=="" and hidden==1:
                    #print("file hidden :",i) # For testing purposes
                    icon=can1.create_image(currentWidthIconPlacement+37.5,currentHeightIconPlacement+37.5,image=icon2_hid)
                    lab1=can1.create_text(currentWidthIconPlacement+37.5,currentHeightIconPlacement+87.5,text=i2,fill="white",width=75,justify=CENTER)
                    IsDirectory=False

            currentWidthIconPlacement+=95

            Grid[numerocolonne].append(i)
            DirGrid[numerocolonne].append(IsDirectory)
            numerocolonne+=1

AfficherDossier(CurrentDir)

win1.mainloop()

#https://github.com/BabdCatha/MyFileExplorer
