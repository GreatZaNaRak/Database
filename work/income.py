from tkinter import *
from PIL import Image, ImageTk
from database import *

class income():
    def __init__(self):

        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\money.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin)
        l = Label(tF, text="Checking Daily Income from Date..")
        l.pack()

        bf1 = Frame(self.cwin,pady=5)
        self.prIn = Label(bf1, text="Date : ")
        self.prInEn = Entry(bf1)

        self.prIn.pack(side=LEFT,padx=10)
        self.prInEn.pack(side=RIGHT)



        bf4 = Frame(self.cwin,pady=5)
        self.ch = Button(bf4, text="CHECK INCOME", width=15,command=self.calculate)
        self.ex = Button(bf4, text ="EXIT", width=15, command=self.cwin.destroy)
        self.ch.pack(side=LEFT,padx=10)
        self.ex.pack(side=RIGHT)

        bf5 = Frame(self.cwin)
        self.label_status = Label(bf5,text="Please fill the date you want to calculate income.\n(Room revenue will be calculated from rooms that are not available on that day.)")

        self.label_status.pack()
        
        tF.grid(row=1)
        bf1.grid(row=2)
        bf4.grid(row=3)
        bf5.grid(row=4)
 
       

        self.cwin.title("Daily Income")
        self.cwin.geometry('450x700')

    def calculate(self):

        dateobj = self.prInEn.get()

        income = incomeDB(dateobj)
        msg = income.calculateTicket()
        ticketmsg = "Ticket income from "+str(dateobj)+" : "+str(msg[1])+ " THB.\n"
        msg2 = income.calculateSellItem()
        itemmsg = "Net worth from product in all store , date:"+str(dateobj)+'\n' + \
            str(msg2[1]) + " THB.\n"
        msg3 = income.calculateRoonIncome()
        roommsg = "Room income from "+str(dateobj)+" : "+str(msg3[1])+ " THB.\n"
        msg4 = income.calculateDinnerIncome()
        dinnermsg = "Dinner income from "+str(dateobj)+" : "+str(msg4[1])+ " THB.\n"
        msg5 = income.calculateFaIncome()
        famsg = "facility income from "+str(dateobj)+" : "+str(msg5[1])+ " THB.\n"
        totalIncome = float(msg[1]) + float(msg3[1]) + float(msg2[1]) + float(msg4[1]) + float(msg5[1])
        totmsg = "Total income in "+ str(dateobj) + " is " + str(totalIncome) + " THB. \n"
        self.label_status.config(text=ticketmsg+"-------------------\n"+itemmsg \
            + "-------------------\n"+roommsg + "-------------------\n"+ dinnermsg + "-------------------\n"+famsg + \
                "-------------------------\n" + totmsg,font=("Courier",10))

