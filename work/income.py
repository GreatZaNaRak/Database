from tkinter import *
from PIL import Image, ImageTk 

class income():
    def __init__(self):

        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\money.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin)
        l = Label(tF, text="Checking Daily Income..")
        l.pack()

        bf1 = Frame(self.cwin,pady=5)
        self.prIn = Label(bf1, text="Product Income: ")
        self.prInEn = Entry(bf1)

        self.prIn.pack(side=LEFT,padx=10)
        self.prInEn.pack(side=RIGHT)

        bf2 = Frame(self.cwin,pady=5)
        self.plIn = Label(bf2, text="     Plays Income: ")
        self.plInEn = Entry(bf2)

        self.plIn.pack(side=LEFT,padx=10)
        self.plInEn.pack(side=RIGHT)

        bf3 = Frame(self.cwin,pady=5)
        self.rIn = Label(bf3, text=" Rooms Income: ")
        self.rInEn = Entry(bf3)

        self.rIn.pack(side=LEFT,padx=10)
        self.rInEn.pack(side=RIGHT)

        bf4 = Frame(self.cwin,pady=5)
        self.ch = Button(bf4, text="CHECK INCOME", width=15)
        self.ex = Button(bf4, text ="EXIT", width=15, command=self.cwin.destroy)
        self.ch.pack(side=LEFT,padx=10)
        self.ex.pack(side=RIGHT)
        
        tF.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf4.grid(row=5)
 
       

        self.cwin.title("Daily Income")
        self.cwin.geometry('450x450')