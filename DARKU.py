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
import os
from tcpgecko import *
import sys

os.system('cls' if os.name == 'nt' else 'clear')

versions = " 1.0"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.BOLD +bcolors.OKBLUE +"     _____             _    _    _ " + bcolors.ENDC)
print(bcolors.BOLD +bcolors.OKBLUE +"    |  __ \           | |  | |  | |" + bcolors.ENDC)
print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | | __ _ _ __| | _| |  | |" + bcolors.ENDC)
print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | |/ _` | '__| |/ / |  | |" + bcolors.ENDC)
print(bcolors.BOLD +bcolors.OKBLUE +"    | |__| | (_| | |  |   <| |__| |" + bcolors.ENDC)
print(bcolors.BOLD +bcolors.OKBLUE +"    |_____/ \__,_|_|  |_|\_\\_____/"+ versions + bcolors.ENDC)
print(bcolors.BOLD +bcolors.OKBLUE +"                                    Created by vincent-coding" + bcolors.ENDC)
time.sleep(1)

theme=input("\n\nWhat theme do you want?\nEnter \"white\" or \"black\".\n")
if theme.lower()=="white":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bcolors.BOLD +bcolors.OKBLUE +"     _____             _    _    _ " + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    |  __ \           | |  | |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | | __ _ _ __| | _| |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | |/ _` | '__| |/ / |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |__| | (_| | |  |   <| |__| |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    |_____/ \__,_|_|  |_|\_\\_____/"+ versions + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"                                    Created by vincent-coding" + bcolors.ENDC)  
    time.sleep(1)
    whiteip=input("\n\nWhat is the ip of the WiiU?\n")
    whitetcp = TCPGecko(whiteip)
    time.sleep(1)
    print('Modification in progress')
    time.sleep(1)    
    whitetcp.pokemem(0x105DD0A8, 0x3F800000)
    whitetcp.s.close()
    print(bcolors.OKGREEN + "Successful modification." + bcolors.ENDC)
elif theme.lower()=="black":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bcolors.BOLD +bcolors.OKBLUE +"     _____             _    _    _ " + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    |  __ \           | |  | |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | | __ _ _ __| | _| |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | |/ _` | '__| |/ / |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |__| | (_| | |  |   <| |__| |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    |_____/ \__,_|_|  |_|\_\\_____/"+ versions + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"                                    Created by vincent-coding" + bcolors.ENDC)  
    time.sleep(1)    
    blackip=input("\n\nWhat is the ip of the WiiU?\n")
    blacktcp = TCPGecko(blackip)
    time.sleep(1)
    print('Modification in progress')
    time.sleep(1)
    blacktcp.pokemem(0x105DD0A8, 0x00000000)
    blacktcp.s.close()
    print(bcolors.OKGREEN + "Successful modification." + bcolors.ENDC)
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(bcolors.BOLD +bcolors.OKBLUE +"     _____             _    _    _ " + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    |  __ \           | |  | |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | | __ _ _ __| | _| |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |  | |/ _` | '__| |/ / |  | |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    | |__| | (_| | |  |   <| |__| |" + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"    |_____/ \__,_|_|  |_|\_\\_____/"+ versions + bcolors.ENDC)
    print(bcolors.BOLD +bcolors.OKBLUE +"                                    Created by vincent-coding" + bcolors.ENDC)   
    time.sleep(1)    
    print(bcolors.FAIL + bcolors.BOLD + "\n\nError, to be able to change the background color of your WiiU menu, you must select a color!" + bcolors.ENDC)

#Created by vincent-coding
