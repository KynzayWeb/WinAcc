import os
import time
from pystyle import *

os.system('cls')
os.system('title WinAcc By Nity Web#0666 ')
os.system('mode 48, 17')
print(Colorate.Vertical(Colors.blue_to_purple , """
        ▄▄▌ ▐ ▄▌▪   ▐ ▄  ▄▄▄·  ▄▄·  ▄▄· 
        ██· █▌▐███ •█▌▐█▐█ ▀█ ▐█ ▌▪▐█ ▌▪
        ██▪▐█▐▐▌▐█·▐█▐▐▌▄█▀▀█ ██ ▄▄██ ▄▄
        ▐█▌██▐█▌▐█▌██▐█▌▐█ ▪▐▌▐███▌▐███▌
         ▀▀▀▀ ▀▪▀▀▀▀▀ █▪ ▀  ▀ ·▀▀▀ ·▀▀▀                                            
""" , 1))

print(Colors.purple + "\n           [1]" + Colors.blue + " actv win 10 pro\n" + Colors.purple + "           [2]" + Colors.blue + " actv win 10 famille\n" + Colors.purple + "           [3]" + Colors.blue + " actv win 10 pro N\n" + Colors.purple + "           [4]" + Colors.blue + " actv win 10 home\n" + Colors.purple + "           [5]" + Colors.blue + " actv win 10 entreprise\n" + Colors.purple + "           [6]" + Colors.blue + " actv win 10 entreprise N\n")
main1 = input(Colors.purple + "<User/>")

def main():
    if main1 == '1':
      pro()
    if main1 == '2':
        fam()
    if main1 == '3':
        pron()
    if main1 == '4':
        hm()
    if main1 == '5':
        entr()
    if main1 == '6':
        entrn()

def pro():
    os.system('start src/pro.exe')
    time.sleep(3.5)
    print(Colors.green + "windows actived :)" + Colors.reset)
def fam():
    os.system('start src/fam.exe')
    time.sleep(3.5)
    print(Colors.green + "windows actived :)" + Colors.reset)
def pron():
    os.system('start src/pron.exe')
    time.sleep(3.5)
    print(Colors.green + "windows actived :)" + Colors.reset)
def hm():
    os.system('start src/hm.exe')
    time.sleep(3.5)
    print(Colors.green + "windows actived :)" + Colors.reset)
def entr():
    os.system('start src/entr.exe')
    time.sleep(3.5)
    print(Colors.green + "windows actived :)" + Colors.reset)
def entrn():
    os.system('start src/entrn.exe')
    time.sleep(3.5)
    print(Colors.green + "windows actived :)" + Colors.reset)



if __name__ == "__main__":
    main()