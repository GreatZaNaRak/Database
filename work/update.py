from tkinter import *
from PIL import Image, ImageTk
from database import *

class upTicket():
    def __init__(self):

        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\ticket.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Typename : ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="New Price: ")
        self.empNameEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=10)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="UPDATE", width=15,command=self.updateTicket)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        moreFoot = Frame(self.cwin)
        self.labet_status = Label(moreFoot,text="Fill typename and updated price")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.labet_status.pack()

        foot.grid(row=2)
        moreFoot.grid(row=3)


        self.cwin.title('Update Ticket')
        self.cwin.geometry('450x500')

    def updateTicket(self) :
        self.cwin.title('Update Complete')
        typename = self.empEn.get()
        newPrice = self.empNameEn.get()
        aTT = TickettypeDB(typename,newPrice)
        retmsg = aTT.updatePrice(newPrice)
        self.labet_status.config(text=retmsg[1])

class upPlay():
    def __init__(self):

        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\p1.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Product Name: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="New Price: ")
        self.empNameEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=10)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="UPDATE", width=15,command=self.updateP)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        moreFoot = Frame(self.cwin)

        self.labet_status = Label(moreFoot,text="fill Product name and new price")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.labet_status.pack()

        foot.grid(row=2)
        moreFoot.grid(row=3)


        self.cwin.title('Update Product name')
        self.cwin.geometry('450x600')

    def updateP(self):

        self.cwin.title("Update complete")
        name = self.empEn.get()
        price = self.empNameEn.get()
        aProd = ProductAndStoreDB(name,price,"0")
        retmsg = aProd.updateProductPrice()
        self.labet_status.config(text=retmsg[1])