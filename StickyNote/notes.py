import tkinter as tk
from tkinter import filedialog, Text
import os 

window = []

def addWindow():
    orther = tk.Tk()
    window.append(orther)

    topframe = tk.Frame(orther, width=230)
    topframe.pack(side='top')

    inlineframe = tk.Frame(topframe, width=170, bg='blue')
    inlineframe.pack(side='left')

    bottomframe = tk.Frame(orther)
    bottomframe.pack(side="bottom")

    bt = tk.Button(orther, text="Add", command=addWindow)
    bt.pack(side = 'right')

    text = Text(bottomframe, height=15, width=30, spacing2=5, spacing3=10)
    text.pack()
    orther.mainloop()

addWindow()