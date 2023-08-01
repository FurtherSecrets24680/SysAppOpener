import tkinter as tk
from PIL import Image, ImageTk
import os

def open_notepad():
    os.system("notepad.exe")

def open_cmd():
    os.system("cmd.exe")

def open_mspaint():
    os.system("mspaint.exe")

def open_task_manager():
    os.system("taskmgr.exe")

def open_powershell():
    os.system("powershell.exe")

def open_calculator():
    os.system("calc.exe")

def open_charmap():
    os.system("charmap.exe")

def open_diskmgmt():
    os.system("diskmgmt.msc")

def open_eventvwr():
    os.system("eventvwr.msc")

def open_perfmon():
    os.system("perfmon.msc")

def open_iexpress():
    os.system("iexpress.exe")

def open_eudcedit():
    os.system("eudcedit.exe")

def open_gpedit():
    os.system("gpedit.msc")

def open_services():
    os.system("services.msc")

def open_regedit():
    os.system("regedit.exe")

def open_winver():
    os.system("winver.exe")

def open_msinfo32():
    os.system("msinfo32.exe")
    
root = tk.Tk()
root.title("SysAppOpener")

img = Image.open("logo.ico")
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)

label = tk.Label(root, text="Click the button to open the desired application:")
label.pack()

button1 = tk.Button(root, text="Open Notepad", command=open_notepad)
button1.pack()

button2 = tk.Button(root, text="Open Command Prompt", command=open_cmd)
button2.pack()

button3 = tk.Button(root, text="Open Paint", command=open_mspaint)
button3.pack()

button4 = tk.Button(root, text="Open Task Manager", command=open_task_manager)
button4.pack()

button5 = tk.Button(root, text="Open Calculator", command=open_calculator)
button5.pack()

button6 = tk.Button(root, text="Open Character Map", command=open_charmap)
button6.pack()

button7 = tk.Button(root, text="Open Disk Management", command=open_diskmgmt)
button7.pack()

button8 = tk.Button(root, text="Open Event Viewer", command=open_eventvwr)
button8.pack()

button9 = tk.Button(root, text="Open Performance Monitor", command=open_perfmon)
button9.pack()

button10 = tk.Button(root, text="Open IExpress", command=open_iexpress)
button10.pack()

button11 = tk.Button(root, text="Open Powershell", command=open_powershell)
button11.pack()

button12 = tk.Button(root, text="Open Private Character Editor", command=open_eudcedit)
button12.pack()

button13 = tk.Button(root, text="Open Group Policy Editor (Windows Pro Only)", command=open_gpedit)
button13.pack()

button14 = tk.Button(root, text="Open Services", command=open_services)
button14.pack()

button15 = tk.Button(root, text="Open Registry Editor", command=open_regedit)
button15.pack()

button16 = tk.Button(root, text="Open Winver (About Windows)", command=open_winver)
button16.pack()

button17 = tk.Button(root, text="Open MsInfo32 (System Information)", command=open_msinfo32)
button17.pack()

root.mainloop()
