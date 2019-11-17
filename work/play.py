from tkinter import *
from PIL import Image, ImageTk 


class pIn():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\p2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.pID = Label(bdF, text="Plays ID: ")
        self.pEn = Entry(bdF)

        self.pName = Label(bdF, text="Plays Name: ")
        self.pNameEn = Entry(bdF)

        self.pAge = Label(bdF, text="Plays Age: ")
        self.pAgeEn = Entry(bdF)

        self.pSta = Label(bdF, text="Plays Status: ")
        self.pStaEn = Entry(bdF)

        self.pPl = Label(bdF, text="Plays Plays: ")
        self.pPlEn = Entry(bdF)

        self.pID.grid(row=0,column=0)
        self.pEn.grid(row=0,column=1, pady=5)
        self.pName.grid(row=1,column=0)
        self.pNameEn.grid(row=1,column=1,pady=5)
        self.pAge.grid(row=2,column=0)
        self.pAgeEn.grid(row=2,column=1,pady=5)
        self.pSta.grid(row=3,column=0)
        self.pStaEn.grid(row=3,column=1,pady=5)
        self.pPl.grid(row=4,column=0)
        self.pPlEn.grid(row=4,column=1,pady=5)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="INSERT", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Insert Plays')
        self.cwin.geometry('450x450')

class pOut():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\p2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.pID = Label(bdF, text="Plays ID: ")
        self.pEn = Entry(bdF)

        self.pName = Label(bdF, text="Plays Name: ")
        self.pNameEn = Entry(bdF)

        self.pID.grid(row=0,column=0)
        self.pEn.grid(row=0,column=1, pady=10)
        self.pName.grid(row=1,column=0)
        self.pNameEn.grid(row=1,column=1)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="DELETE", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Delete Plays')
        self.cwin.geometry('450x450')

class pQue():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\p2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.pID = Label(bdF, text="Plays ID: ")
        self.pEn = Entry(bdF)

        self.pName = Label(bdF, text="Plays Name: ")
        self.pNameEn = Entry(bdF)

        self.pAge = Label(bdF, text="Plays Age: ")
        self.pAgeEn = Entry(bdF)

        self.pSta = Label(bdF, text="Plays Status: ")
        self.pStaEn = Entry(bdF)

        self.pPl = Label(bdF, text="Plays Plays: ")
        self.pPlEn = Entry(bdF)

        self.pID.grid(row=0,column=0)
        self.pEn.grid(row=0,column=1, pady=5)
        self.pName.grid(row=1,column=0)
        self.pNameEn.grid(row=1,column=1,pady=5)
        self.pAge.grid(row=2,column=0)
        self.pAgeEn.grid(row=2,column=1,pady=5)
        self.pSta.grid(row=3,column=0)
        self.pStaEn.grid(row=3,column=1,pady=5)
        self.pPl.grid(row=4,column=0)
        self.pPlEn.grid(row=4,column=1,pady=5)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="SEARCH", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Query Plays')
        self.cwin.geometry('450x450')
