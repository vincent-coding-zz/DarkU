# DarkU
# Created by vincent-coding
# Licences : MIT

# Si vous décidez d'utiliser le code source, mentionnez-moi comme créateur de base !
# If you decide to use the source code, please mention me as the basic creator!

# START
# !usr/bin/env python
# -*- coding: utf-8 -*-

#Import
import time
from tkinter import *
import tkinter.messagebox
import os
from tcpgecko import *
import sys

os.system('cls' if os.name == 'nt' else 'clear')

versions = " 1.2"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def checkinject():
    ip = wiiuip.get()
    colors = listecouleur.get()
    if ip != "":
        if colors=="White":
            wtcp = TCPGecko(ip)
            wtcp.pokemem(0x105DD0A8, 0x3F800000)
            wtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")           
        elif colors=="Black":
            btcp = TCPGecko(ip)
            btcp.pokemem(0x105DD0A8, 0x00000000)
            btcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")
        elif colors=="Light grey":
            lgtcp = TCPGecko(ip)
            lgtcp.pokemem(0x105DD0A8, 0x3E800000)
            lgtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")  
        elif colors=="Grey":
            gtcp = TCPGecko(ip)
            gtcp.pokemem(0x105DD0A8, 0x3D800000)
            gtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")
        elif colors=="Dark grey":
            dgtcp = TCPGecko(ip)
            dgtcp.pokemem(0x105DD0A8, 0x3C800000)
            dgtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")   
        elif colors=="Very dark grey":
            vdgtcp = TCPGecko(ip)
            vdgtcp.pokemem(0x105DD0A8, 0x3B800000)
            vdgtcp.s.close()
            tkinter.messagebox.showinfo("DarkU - "+versions, "Injection successful!")
    else:
        tkinter.messagebox.showerror("DarkU - "+versions, "Please fill in the \"wiiu ip\" field")

# Interface
main = Tk()
 
wiiuip = StringVar()
listecouleur = StringVar()
listecouleur.set("White")

#Info de la fenetre
largeur      = 300
hauteur      = 175
largeurEcran = main.winfo_screenwidth()
hauteurEcran = main.winfo_screenheight()
x            = (largeurEcran / 2) - (largeur / 2)
y            = (hauteurEcran / 2) - (hauteur /2)
main.geometry('%dx%d+%d+%d' % (largeur, hauteur, x, y))
main.resizable(width = False, height = False)
main.title("DarkU - "+versions)

#Component
content = Frame(width=250, height=15).pack()
iplabel = Label(content, text="WiiU ip").pack()
ipentry = Entry(content, textvariable=wiiuip).pack()
listecolorsmenu = OptionMenu(content, listecouleur, "White", "Light grey", "Grey", "Dark grey", "Very dark grey", "Black").pack(pady=5)
inject = Button(content, text="Inject", command=checkinject).pack(pady=5)

info = Label(main, text="Created by vincent-coding").pack(side=BOTTOM)

# END
main.mainloop()
#Created by vincent-coding
