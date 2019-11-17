from tkinter import *
from gui import *
from userGUI import *
from PIL import Image, ImageTk 

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

class Win():
    def __init__(self):

        self.i = 0
    
        rt = Tk()

        # head
        topFrame = Frame(rt, pady=30)

        head = Label(rt, text='Welcome to Database Application',pady=10)
        head.pack()

        img = Image.open('images/male.png')
        img = img.resize((150, 150), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(img)
        my_label = Label(topFrame, image=my_img)
        my_label.pack()

        topFrame.pack()

        # body

        bodyFrame = Frame(rt)

        self.l1 = Label(bodyFrame, text='Username: ')
        self.e1 = Entry(bodyFrame)
        self.l2 = Label(bodyFrame, text='Password: ')
        self.e2 = Entry(bodyFrame, show='*')

        self.l1.grid(row=0,column=0,padx=10,pady=5); self.l2.grid(row=1,column=0)
        self.e1.grid(row=0,column=1); self.e2.grid(row=1,column=1)


        bodyFrame.pack()

        # footer

        footFrame = Frame(rt, pady=30)

        self.logBut = Button(footFrame, text='Login', width=7, command=combine_funcs(self.log, rt.destroy))
        self.exitBut = Button(footFrame, text='Exit', width=7, command=rt.destroy)

        self.logBut.grid(row=0,column=0)
        self.exitBut.grid(row=0,column=1,padx=5)
        footFrame.pack()

        # temp frame

        # run window

        rt.title('Login Window')
        rt.geometry('500x500')
        rt.mainloop()
    
    
    def log(self):
        self.i += 1
        self.username = self.e1.get()
        self.psw = self.e2.get()
        print(self.username)
        
        
    
    def exit(self):
        exit(0)


a = Win()
d = {'great':'pass'}
if a.i != 0: 
    if a.username.lower() == 'admin' and a.psw.lower() == 'admin': Window()
    else: 
        if a.username.lower() in d and a.psw.lower() == d[a.username.lower()]: UserWindow()
