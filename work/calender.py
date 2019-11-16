from tkinter import *
import tkinter as tk
import time

class calender():
    def __init__(self):

        root = tk.Tk()
        root.title("ticket reserved")
        root.geometry('250x150+200+200')

        self.b = tk.Button(root, text="OK", command=root.destroy, bg="grey")

        self.L = Label(root, text="You have reserved a ticket !!!")
        self.L.pack(pady=10)

        self.aa = Label(root, text=str(time.asctime()))
        self.aa.pack(pady=10)

        self.b.pack(pady=10)


        root.mainloop()
    
