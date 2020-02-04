from tkinter import *
from PIL import Image, ImageTk 
from database import *

class billCheck():
    def __init__(self):

        self.cwin = Toplevel()

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\money.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)


        bf1 = Frame(self.cwin,pady=5)
        self.cIn = Label(bf1, text="    Billing ID: ")
        self.cInEn = Entry(bf1)

        self.cIn.pack(side=LEFT,padx=10)
        self.cInEn.pack(side=RIGHT)



        bf5 = Frame(self.cwin,pady=5)
        self.ch = Button(bf5, text="CHECK BILL", width=15,command=self.getInfo)
        self.ex = Button(bf5, text ="EXIT", width=15, command=self.cwin.destroy)

        self.ch.pack(side=LEFT,padx=10)
        self.ex.pack(side=RIGHT)

        bf6 = Frame(self.cwin)
        self.label_status = Label(bf6,text="Fill your billing ID to see what do you will pay from bill.")


        self.label_status.pack()
        
        
        bf1.grid(row=2)
        bf5.grid(row=3)
        bf6.grid(row=4)

       

        self.cwin.title("Checking Billing")
        self.cwin.geometry('450x700')

    def getInfo(self):
        bid = self.cInEn.get()
        aBill = CheckBillingDB(bid)
        retmsg = aBill.getRoomBill()
        roomInfo = "***Room Bill***\n"
        for e in retmsg[1]:
            roomInfo += "RoomNo : " + str(e[0]) + "\n" + \
                "Room Type : " + str(e[1]) + "\n" + \
                    "Checkin Date : " + str(e[2])  + "\n" + \
                        "Checkout Date : " + str(e[3]) + "\n"
            rp = aBill.getRoomPrice(str(e[1]))
            for f in rp[1]:
                roomInfo += "Price per day : " + str(f)+"\n"
        if roomInfo == "***Room Bill***\n" : roomInfo = "**no Room Bill**\n"
        dmsg = aBill.getDinnerBill()
        dinnerInfo = "**Dinner Bill**\n"
        for g in dmsg[1] :
            dinnerInfo += "Total dinner Price in " +  str(g[0])+ " : " +str(g[1]) + "\n"
        if dinnerInfo == "**Dinner Bill**\n" : dinnerInfo = '**No Dinner bill**\n'
        fmsg = aBill.getFaBill()
        FaInfo = "***Facility Bill***\n"
        for e in fmsg[1]:
            FaInfo += "Facility Name : " + str(e[0]) + "\n"
            rp = aBill.getFaPrice(str(e[0]))
            for f in rp[1]:
                FaInfo += "Price : " + str(f)+"\n"
        if FaInfo == "***Facility Bill***\n" : FaInfo = "**no Facility Bill**\n"        
        self.label_status.config(text=roomInfo+"/////////////////////\n"+dinnerInfo+"/////////////////////\n"+FaInfo)


    

class billPay():
    def __init__(self):

        self.cwin = Toplevel()

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\money.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        bf2 = Frame(self.cwin,pady=5)
        self.rIn = Label(bf2, text="Customer ID: ")
        self.cidEn = Entry(bf2)

        self.rIn.pack(side=LEFT,padx=10)
        self.cidEn.pack(side=RIGHT)

        bf3 = Frame(self.cwin,pady=5)
        self.rIn = Label(bf3, text="CreditCard NO: ")
        self.CCNEn = Entry(bf3)

        self.rIn.pack(side=LEFT,padx=10)
        self.CCNEn.pack(side=RIGHT)

        bf4 = Frame(self.cwin,pady=5)
        self.paIn = Label(bf4, text="  Payment Date:")
        self.PDEn = Entry(bf4)
        
        self.paIn.pack(side=LEFT,padx=10)
        self.PDEn.pack(side=RIGHT)

        bf5 = Frame(self.cwin,pady=5)
        self.ch = Button(bf5, text="PAY", width=15,command=self.addPayment)
        self.ex = Button(bf5, text ="EXIT", width=15, command=self.cwin.destroy)

        self.ch.pack(side=LEFT,padx=10)
        self.ex.pack(side=RIGHT)

        bf6 = Frame(self.cwin)
        self.label_status = Label(bf6,text="please fill the information \n You will get Billing ID that use for room booking \n and other service.")

        self.label_status.pack()
        
        
        bf2.grid(row=2)
        bf3.grid(row=3)
        bf4.grid(row=4)
        bf5.grid(row=5)
        bf6.grid(row=6)
 
       

        self.cwin.title("Payment")
        self.cwin.geometry('450x600')

    def addPayment(self):

        self.cwin.title("Payment Complete")
        cid = self.cidEn.get()
        cdc = self.CCNEn.get()
        date = self.PDEn.get()
        aBill = BillingDB(cid,cdc,date)
        retmsg = aBill.addBilling(aBill.generateLatestBillID())
        self.label_status.config(text=retmsg[1])



        