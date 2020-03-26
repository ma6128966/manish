import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *
 
root = Tk()
root.minsize(300,300)
root.title("Music Player")
 
listofsongs = []
realnames = []
 
v = StringVar()
songlabel = Label(root,textvariable=v,width=35)
 
index = 0
 
def directorychooser():
 
    directory = askdirectory()
    os.chdir(directory)
 
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
 
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
 
 
            listofsongs.append(files)
 
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    pygame.mixer.music.queue(listofsongs[index + 1])
    updatelabel()
 
directorychooser()

volm = DoubleVar()
vol = Scale(root, variable = volm, activebackground = "Black", troughcolor = "Blue").grid(row = 13, column = 2)
volm.set(100)

#print(volm.get()/100.0)
def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname
 
 
 
def nextsong():
    global index
    if index == len(realnames) - 1:
        index = 0
    else:
    	index += 1
    resumesong()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    if index == len(realnames) - 1:
        pygame.mixer.music.queue(listofsongs[0])
    else:
        pygame.mixer.music.queue(listofsongs[index + 1])
    updatelabel()
 
def prevsong():
    global index
    if index == 0:
        index = len(realnames) - 1
    else:
        index -= 1
    resumesong()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    if index == len(realnames) - 1:
        pygame.mixer.music.queue(listofsongs[0])
    else:
        pygame.mixer.music.queue(listofsongs[index + 1])
    updatelabel()
 
 
def pausesong():
    pygame.mixer.music.pause()
    resumebutton = Button(root, text = "Resume", command = resumesong)
    resumebutton.grid(row = 41, column = 2)
    v.set("")
    updatelabel()
    #return songname
 
def resumesong():
    pygame.mixer.music.unpause()
    pausebutton = Button(root,text='Pause', command = pausesong)
    pausebutton.grid(row = 41, column = 2)
    updatelabel()
 
def changevol():
    pygame.mixer.music.set_volume(volm.get() / 100.0)
 
listbox = Listbox(root, background = "Blue")
listbox.grid(row = 1, columnspan = 30, rowspan = 40)
 
#listofsongs.reverse()
realnames.reverse()
 
for items in realnames:
    listbox.insert(0,items)
 
realnames.reverse()
#listofsongs.reverse()
 
 
nextbutton = Button(root,text = 'Next Song', command = nextsong)
nextbutton.grid(row = 41, column = 0)
 
previousbutton = Button(root,text = 'Previous Song', command = prevsong)
previousbutton.grid(row = 41, column = 1, sticky = W)
 
pausebutton = Button(root,text='Pause', command = pausesong)
pausebutton.grid(row = 41, column = 2)

volbutton = Button(root, text = "Change Vol", command = changevol)
volbutton.grid(row = 32, column =2)


""" 
nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
"""
songlabel.grid(row = 42)

root.mainloop()
