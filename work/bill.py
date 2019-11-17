from tkinter import *
from PIL import Image, ImageTk 

class billCheck():
    def __init__(self):

        self.cwin = Toplevel()

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\money.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)


        bf1 = Frame(self.cwin,pady=5)
        self.cIn = Label(bf1, text="    Customer ID: ")
        self.cInEn = Entry(bf1)

        self.cIn.pack(side=LEFT,padx=10)
        self.cInEn.pack(side=RIGHT)

        bf2 = Frame(self.cwin,pady=5)
        self.plIn = Label(bf2, text="           Billing ID: ")
        self.plInEn = Entry(bf2)

        self.plIn.pack(side=LEFT,padx=10)
        self.plInEn.pack(side=RIGHT)

        bf3 = Frame(self.cwin,pady=5)
        self.rIn = Label(bf3, text="CreditCard NO: ")
        self.rInEn = Entry(bf3)

        self.rIn.pack(side=LEFT,padx=10)
        self.rInEn.pack(side=RIGHT)


        bf5 = Frame(self.cwin,pady=5)
        self.ch = Button(bf5, text="CHECK BILL", width=15)
        self.ex = Button(bf5, text ="EXIT", width=15, command=self.cwin.destroy)

        self.ch.pack(side=LEFT,padx=10)
        self.ex.pack(side=RIGHT)
        
        
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf5.grid(row=6)
 
       

        self.cwin.title("Checking Billing")
        self.cwin.geometry('450x450')

class billPay():
    def __init__(self):

        self.cwin = Toplevel()

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\money.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)


        bf1 = Frame(self.cwin,pady=5)
        self.cIn = Label(bf1, text="Ticket Billing ID: ")
        self.cInEn = Entry(bf1)

        self.cIn.pack(side=LEFT,padx=10)
        self.cInEn.pack(side=RIGHT)

        bf2 = Frame(self.cwin,pady=5)
        self.plIn = Label(bf2, text="Room Billing ID: ")
        self.plInEn = Entry(bf2)

        self.plIn.pack(side=LEFT,padx=10)
        self.plInEn.pack(side=RIGHT)

        bf3 = Frame(self.cwin,pady=5)
        self.rIn = Label(bf3, text="CreditCard NO: ")
        self.rInEn = Entry(bf3)

        self.rIn.pack(side=LEFT,padx=10)
        self.rInEn.pack(side=RIGHT)

        bf4 = Frame(self.cwin,pady=5)
        self.paIn = Label(bf4, text="  Payment Date:")
        self.paInEn = Entry(bf4)
        
        self.paIn.pack(side=LEFT,padx=10)
        self.paInEn.pack(side=RIGHT)

        bf5 = Frame(self.cwin,pady=5)
        self.ch = Button(bf5, text="PAY", width=15)
        self.ex = Button(bf5, text ="EXIT", width=15, command=self.cwin.destroy)

        self.ch.pack(side=LEFT,padx=10)
        self.ex.pack(side=RIGHT)
        
        
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf4.grid(row=5)
        bf5.grid(row=6)
 
       

        self.cwin.title("Payment")
        self.cwin.geometry('450x450')