import tkinter as tk
import os

def open_notepad():
    os.system("notepad.exe")

def open_cmd():
    os.system("cmd.exe")

def open_mspaint():
    os.system("mspaint.exe")

def open_task_manager():
    os.system("taskmgr.exe")

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

root = tk.Tk()
root.title("Useful Application Utility")

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

root.mainloop()
