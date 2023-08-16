import tkinter as tk

from tkinter import *

root = Tk()
Label(root, text = "Name").grid(row = 0, sticky = W)
Label(root, text = "NRIC").grid(row = 1, sticky = W)
Label(root, text = "Birth Date (DD/MM/YYYY)").grid(row = 2, sticky = W)


Name = Entry(root)
Nric = Entry(root)
Bdate = Entry(root)



Name.grid(row = 0, column = 1)
Nric.grid(row = 1, column = 1)
Bdate.grid(row = 2, column = 1)


def getInput():

    a = Name.get()
    b = Nric.get()
    c = Bdate.get()
    
    root.destroy()

    global params
    params = [a,b,c]


Button(root, text = "submit",
           command = getInput).grid(row = 5, sticky = W)
mainloop()

root.mainloop() 