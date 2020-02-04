from tkinter import *
from PIL import Image, ImageTk
from database import *

class user():
    def __init__(self):

        self.cwin = Toplevel()

        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\user2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="User ID: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="User FName: ")
        self.empNameEn = Entry(bdF)

        self.empAge = Label(bdF, text="User LName: ")
        self.empAgeEn = Entry(bdF)

        self.empSta = Label(bdF, text="User Phone: ")
        self.empStaEn = Entry(bdF)

        self.empEm = Label(bdF, text="User Email: ")
        self.empEmEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=5)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1,pady=5)
        self.empAge.grid(row=2,column=0)
        self.empAgeEn.grid(row=2,column=1,pady=5)
        self.empSta.grid(row=3,column=0)
        self.empStaEn.grid(row=3,column=1,pady=5)
        self.empEm.grid(row=4,column=0)
        self.empEmEn.grid(row=4,column=1,pady=5)


        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="SEARCH", width=15,command=self.queryuser)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        moreFoot = Frame(self.cwin)
        self.label_status = Label(moreFoot,text="please fill some field")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        foot.grid(row=2)
        moreFoot.grid(row=3)


        self.cwin.title('Query User')
        self.cwin.geometry('450x600')

    def queryuser(self):

        self.cwin.title()
        cid = self.empEn.get()
        fname = self.empNameEn.get()
        lname = self.empAgeEn.get()
        phone = self.empStaEn.get()
        email = self.empEmEn.get()
        aCustomer = CustomerDB(cid,fname,lname,phone,email)
        retmsg = aCustomer.queryuser()
        reservermsg = "- Reserver-\n"
        for e in retmsg[1]:
            if len(e) == 0 :
                reservermsg = ""
            else : 
                reservermsg += "Customer_ID :"+ str(e[0]) + "\n" +\
                            "Name : "+str(e[1])+" "+str(e[2])+"\n"+\
                            "Phone : "+str(e[3])+" E-mail : "+str(e[4])+"\n"
        if reservermsg == "- Reserver-\n" : reservermsg = ""
        guestmsg = "-Guest-\n"
        for e in retmsg[2]:
            if len(e) == 0 :
                guestmsg = ""
            else : 
                guestmsg += "Customer_ID :"+ str(e[0]) + "\n" +\
                            "Name : "+str(e[1])+" "+str(e[2])+"\n"+\
                            "Phone : "+str(e[3])+" E-mail : "+str(e[4])+"\n"
        if guestmsg == "-Guest-\n" : guestmsg = ""
        if guestmsg == "" and reservermsg == "" : merge = "not found"
        else : merge = reservermsg+guestmsg
        self.label_status.config(text=merge)
            


class roomer():
    def __init__(self):

        self.cwin = Toplevel()

        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\user2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Billing ID: ")
        self.empEn = Entry(bdF)



        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=5)


        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="SEARCH", width=15,command=self.getRoomerInfo)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        moreFoot = Frame(self.cwin)
        self.label_status = Label(moreFoot,text="please fill some field")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        foot.grid(row=2)
        moreFoot.grid(row=3)


        self.cwin.title('Query Roomer')
        self.cwin.geometry('450x600')

    def getRoomerInfo(self):

        bid = self.empEn.get()
        aBill = CheckBillingDB(bid)
        cidlist = aBill.getCusID()
        if cidlist[1] != None:
            roomInfo = aBill.getRoomBill()
            strrommif = "*****Room Info****\n"
            for e in roomInfo[1]:
                strrommif += "RoomNo : " + str(e[0]) + "\n" + \
                "Room Type : " + str(e[1]) + "\n" + \
                    "Checkin Date : " + str(e[2])  + "\n" + \
                        "Checkout Date : " + str(e[3]) + "\n"
            aCus = cidlist[1][0]
            cusinfo = aBill.getGuestInfo(aCus)
            strguest = "***Guest Info***\n"
            strguest += "Name :" + str(cusinfo[1][0])+" "+ str(cusinfo[1][1]) + "\n" + \
                        "Phone : " + str(cusinfo[1][2]) + "\n" + \
                        "E-Mail : " + str(cusinfo[1][3])
            self.label_status.config(text=strrommif + strguest )
        else : 
            aCus = "bill not found"
            self.label_status.config(text=str(aCus))