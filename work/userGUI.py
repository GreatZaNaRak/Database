from tkinter import *
from bill import *
from calender import *
import time
from PIL import Image, ImageTk
from database import * 

class UserWindow():
    def __init__(self):

        root = Tk()
        
        header = Label(root, text="Welcome User..")
        header.pack()

        # picture

        picFrame = Frame(root)

        img = Image.open('images/user.png')
        img = img.resize((350, 250), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(img)
        my_label = Label(picFrame, image=my_img)
        my_label.pack()

        picFrame.pack()

        # button
        bdFrame = Frame(root, pady=10)

        r1 = Frame(bdFrame)

        self.ticketButton = Button(r1, text="BUY TICKET", width=15, command=self.popTicket)
        self.roomButton = Button(r1, text="BUY ROOM", width=15, command=self.popRoom)

        self.ticketButton.pack(side=LEFT, padx=10)
        self.roomButton.pack(side=RIGHT)

        r2 = Frame(bdFrame, pady=10)

        self.checkInfo = Button(r2, text="MY INFO", width=15, command=self.popMyinfo)
        self.checkBill = Button(r2, text="BILL INFO", width=15, command=self.popBill)

        self.checkInfo.pack(side=LEFT, padx=10)
        self.checkBill.pack(side=RIGHT)

        r3 = Frame(bdFrame, pady=3)

        self.find = Button(r3, text="SEARCH PLAYS", width=15, command=self.popSearchPlays)
        self.exBut = Button(r3, text="PAYMENT", width=15, command=self.popPayment)

        self.find.pack(side=LEFT, padx=10)
        self.exBut.pack(side=RIGHT)



        r1.pack()
        r2.pack()
        r3.pack()
        bdFrame.pack()
        # show

        root.title("Databse GUI")
        root.geometry('450x450')
        root.mainloop()
    

    def popTicket(self):
        t = ticketWin("buying ticket")
    
    def popRoom(self):
        r = roomWin("buying room")
    
    def popMyinfo(self):
        m = myinfoWin("my information")
    
    def popSearchPlays(self):
        p = searchPlaysWin("search plays")

    def popBill(self):
        b = billCheck()
    
    def popPayment(self):
        p2 = billPay()

class ticketWin():
    def __init__(self, title):

        self.cwin = Toplevel()

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\ticket.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image
        background_label.grid(row=0,column=0)

        bf0 = Frame(self.cwin,pady=3)
        self.l0 = Label(bf0, text="Date(yyyy-mm-dd): ")
        self.e0 = Entry(bf0)

        self.l0.pack(side=LEFT,padx=5)
        self.e0.pack(side=RIGHT)

        bf1 = Frame(self.cwin)
        self.l1 = Label(bf1, text="   TypeName:")
        self.e1 = Entry(bf1)

        self.l1.pack(side=LEFT,padx=5)
        self.e1.pack(side=RIGHT)

        bf2 = Frame(self.cwin,pady=3)
        self.l2 = Label(bf2, text="CustomerID:")
        self.e2 = Entry(bf2)

        self.l2.pack(side=LEFT,padx=5)
        self.e2.pack(side=RIGHT)

        bf3 = Frame(self.cwin)
        self.l3 = Label(bf3, text="        Amount: ")
        self.e3 = Entry(bf3)

        self.l3.pack(side=LEFT,padx=5)
        self.e3.pack(side=RIGHT)



        bf7 = Frame(self.cwin,pady=5)
        self.button_submit=Button(bf7, text ="BUY", width=10, command=self.tick)
        self.button_exit=Button(bf7, text="EXIT", width=10, command=self.cwin.destroy)

        bf8 = Frame(self.cwin)

        self.label_status = Label(bf8,text="plase fill infomation")

        self.button_submit.pack(side=LEFT, padx=10)
        self.button_exit.pack(side=RIGHT)
        self.label_status.pack()
        
        bf0.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf7.grid(row=5)
        bf8.grid(row=6)

        self.cwin.title(title)
        self.cwin.geometry('450x600')

    def tick(self):
        # do something
        self.cwin.title("Reserved")
        date = self.e0.get()
        dname = "amusement"
        tyname = self.e1.get()
        cid = self.e2.get()
        ys = date.split("-")
        year_sell = ys[0]
        amnt = self.e3.get()
        aTicket = TicketDB(date,dname,tyname,cid,year_sell,amnt)
        retmsg = aTicket.reserveTicket()
        if retmsg[0] == "0":
            self.label_status.config(text="Your Ticket No:" + str(retmsg[1][0]))
        else : self.label_status.config(text=retmsg[1])
        calender()

class roomWin():
    def __init__(self, title):

        self.cwin = Toplevel()
        self.i = 1

        C = Canvas(self.cwin, bg="blue", height=50, width=50)

        s = "images\\room" + str(self.i) +".png"

        filename1 = PhotoImage(file = s)

        #self.file = str(self.f)+str(self.i)
       
        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin,pady=10)


        b1 = Button(tF, text='<<', command=self.decre)
        b2 = Button(tF, text='>>', command=self.incre)

        b1.pack(side=LEFT,padx=10)
        b2.pack(side=RIGHT)

        bf0 = Frame(self.cwin, pady=5)
        self.l0 = Label(bf0, text="Room NO: ")
        self.e0 = Entry(bf0)

        self.l1 = Label(bf0, text="Type:")
        self.e1 = Entry(bf0)

        self.l0.grid(row=1,column=0)
        self.e0.grid(row=1,column=1)
        self.l1.grid(row=1,column=2,padx=15)
        self.e1.grid(row=1,column=3)

        bf1 = Frame(self.cwin, pady=5)
        self.l2 = Label(bf1, text="    Billing ID:")
        self.e2 = Entry(bf1)

        self.l3 = Label(bf1, text="Phone")
        self.e3 = Entry(bf1)

        self.l2.grid(row=2,column=0)
        self.e2.grid(row=2,column=1)
        self.l3.grid(row=2,column=2,padx=15)
        self.e3.grid(row=2,column=3)

        bf2 = Frame(self.cwin, pady=5)
        self.l4 = Label(bf2, text="      Check_In Date:")
        self.e4 = Entry(bf2)

        self.l5 = Label(bf2, text="Year:")
        self.e5 = Entry(bf2)

        self.l4.grid(row=3,column=0)
        self.e4.grid(row=3,column=1,padx=5)
        self.l5.grid(row=3,column=2)
        self.e5.grid(row=3,column=3)

        bf3 = Frame(self.cwin, pady=5)
        self.l6 = Label(bf3, text=" Check_Out Date:")
        self.e6 = Entry(bf3)


        self.l6.grid(row=3,column=0)
        self.e6.grid(row=3,column=1,padx=5)


        bf5 = Frame(self.cwin,pady=5)
        self.button_submit=Button(bf5, text ="BUY", width=10,command=self.buyRoom)
        self.button_exit=Button(bf5, text="EXIT", width=10, command=self.cwin.destroy)

        bf6 = Frame(self.cwin)
        self.label_status = Label(bf6,text="You can see empty room and fill in the field\nRoom type and Price:\n"+ \
                             "Single room 1800.00 | Double room 2500.00 \n Triple room 3200.00 | King-Sized 3500.00 \n"+ \
                                 "Studio room 1500.00")
        

        self.button_submit.pack(side=LEFT,padx=10)
        self.button_exit.pack(side=RIGHT)
        self.label_status.pack()
        
        tF.grid(row=1,column=0,padx=50)
        bf0.grid(row=2)
        bf1.grid(row=3)
        bf2.grid(row=4)
        bf3.grid(row=5)
        bf5.grid(row=7)
        bf6.grid(row=8)


        self.cwin.title(title)
        self.cwin.geometry('450x600')

    def buyRoom(self):
        room_no = self.e0.get()
        Dname = "accommodation"
        billingID = self.e2.get()
        r_type = self.e1.get()
        phone = self.e3.get()
        in_year = self.e5.get()
        checkin_date = self.e4.get()
        checkout_date = self.e6.get()

        aRoom = RoomDB(room_no,Dname,billingID,r_type,phone,in_year,checkin_date,checkout_date)
        retmsg = aRoom.bookingRoom()

        self.label_status.config(text=retmsg[1])

    def incre(self):

        self.i = (self.i + 1) % 3

        s = "images\\room" + str(self.i) +".png"

        filename1 = PhotoImage(file = s)

        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)

    def decre(self):

        self.i = (self.i - 1) % 3

        s = "images\\room" + str(self.i) +".png" 

        filename1 = PhotoImage(file = s)

        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)

class myinfoWin():
    def __init__(self, title):

        self.cwin = Toplevel()


        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\user2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image
        background_label.grid(row=0,column=0)

        bf0 = Frame(self.cwin,pady=2)
        self.l0 = Label(bf0, text="First Name: ")
        self.e0 = Entry(bf0)

        self.l0.pack(side=LEFT)
        self.e0.pack(side=RIGHT)

        bf1 = Frame(self.cwin,pady=2)
        self.l1 = Label(bf1, text="   Last Name: ")
        self.e1 = Entry(bf1)

        self.l1.pack(side=LEFT)
        self.e1.pack(side=RIGHT)



        bf5 = Frame(self.cwin,pady=10)
        self.searchBut = Button(bf5, text="SEARCH", width=10, command=self.getInfo)
        self.exitBut = Button(bf5, text="EXIT", command=self.cwin.destroy, width=10)

        bf6 = Frame(self.cwin)
        self.label_status = Label(bf6,text="fill your firstname and lastname\nto get your info")

        self.searchBut.pack(side=LEFT,padx=10)
        self.exitBut.pack(side=RIGHT)
        self.label_status.pack()

        bf0.grid(row=1,column=0)
        bf1.grid(row=2,column=0)
        bf5.grid(row=3,column=0)
        bf6.grid(row=4)



        self.cwin.title(title)
        self.cwin.geometry('450x600')

    def getInfo(self):
        self.cwin.title()
        fname = self.e0.get()
        lname = self.e1.get()
        aCustomer = CustomerDB("idc",fname,lname,"XXX","XXX")
        retmsg = aCustomer.usergetinfo()
        reservermsg = "-You Are Reserver-\n"
        for e in retmsg[1]:
            if len(e) == 0 :
                reservermsg = ""
            else : 
                reservermsg += "Customer_ID :"+ str(e[0]) + "\n" +\
                            "Name : "+str(e[1])+" "+str(e[2])+"\n"+\
                            "Phone : "+str(e[3])+" E-mail : "+str(e[4])+"\n"
        if reservermsg == "-You Are Reserver-\n" : reservermsg = ""
        guestmsg = "-You Are Guest-\n"
        for e in retmsg[2]:
            if len(e) == 0 :
                guestmsg = ""
            else : 
                guestmsg += "Customer_ID :"+ str(e[0]) + "\n" +\
                            "Name : "+str(e[1])+" "+str(e[2])+"\n"+\
                            "Phone : "+str(e[3])+" E-mail : "+str(e[4])+"\n"
        if guestmsg == "-You Are Guest-\n" : guestmsg = ""
        if guestmsg == "" and reservermsg == "" : merge = "not found"
        else : merge = reservermsg+guestmsg
        self.label_status.config(text=merge)

        """self.e1.insert(0, 'todo')
        self.e2.insert(0, 'todo')
        self.e3.insert(0, 'todo')
        self.e4.insert(0, 'todo')"""



class searchPlaysWin():
    def __init__(self, title):

        self.cwin = Toplevel()
        self.i = 1

        C = Canvas(self.cwin, bg="blue", height=50, width=50)

        s = "images\\p" + str(self.i+1) +".png"

        filename1 = PhotoImage(file = s)

        #self.file = str(self.f)+str(self.i)
       
        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin,pady=15)


        b1 = Button(tF, text='<<', command=self.decre)
        b2 = Button(tF, text='>>', command=self.incre)

        b1.pack(side=LEFT,padx=10)
        b2.pack(side=RIGHT)


        bf6 = Frame(self.cwin,pady=5)
        self.button_submit=Button(bf6, text ="LIST", width=10, command=self.search)
        self.button_exit=Button(bf6, text="EXIT", width=10, command=self.cwin.destroy)

        bf7 = Frame(self.cwin)
        self.list_label = Label(bf7,text="Press 'LIST' to list all Rides")

        self.button_submit.pack(side=LEFT,padx=10)
        self.button_exit.pack(side=RIGHT)
        self.list_label.pack()

        tF.grid(row=1)
        bf6.grid(row=2,column=0)
        bf7.grid(row=3)


        self.cwin.title(title)
        self.cwin.geometry('450x600')

    def incre(self):

        self.i = (self.i + 1) % 4


        s = "images\\p" + str(self.i+1) +".png"

        filename1 = PhotoImage(file = s)

        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)

    def decre(self):

        self.i = (self.i - 1) % 4

        s = "images\\p" + str(self.i+1) +".png" 

        filename1 = PhotoImage(file = s)

        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)
    
    def search(self):
        aPlays = playDB("x","x","x-x","x","x")
        retmsg = aPlays.listAllPlay()
        output  = ""
        for e in retmsg[1]:
            output += "Rides name : "+str(e[0])+" Time Avalable :" + str(e[1]) + "-" + str(e[2]) + "\n"
        self.list_label.config(text=output)
        """self.e1.delete(0, END)
        self.e1.insert(0, 'todo')
        self.e2.delete(0, END)
        self.e2.insert(0, 'todo')"""



#UserWindow()