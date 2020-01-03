"""
Author: Nguyen Dinh Quan 
Base on Video source: https://www.youtube.com/watch?v=jE-SpRI3K5g&t=12s
Simple app run another app
"""

import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess, sys
# Define the opener to open file  
opener ="open" if sys.platform == "darwin" else "xdg-open"

root = tk.Tk()
apps = []
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/home/quan/Documents", title="Select File", 
                                            filetypes=(("text", "*.txt"), ("all files", "*.*")))
    apps.append(filename)

    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()
def runApps():
    for app in apps:
        subprocess.call([opener, app])

canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File",padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()    

runApps = tk.Button(root, text="Run Apps",padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()    

root.mainloop() 