from tkinter import *
#from database import *
from calender import *
import time
from PIL import Image, ImageTk

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

        self.checkInfo = Button(r2, text="MY INFO", width=15)
        self.checkBill = Button(r2, text="BILL INFO", width=15)

        self.checkInfo.pack(side=LEFT, padx=10)
        self.checkBill.pack(side=RIGHT)

        r3 = Frame(bdFrame, pady=3)

        self.find = Button(r3, text="SEARCH ROOM", width=15)
        self.exBut = Button(r3, text="PAYMENT", width=15)

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

class ticketWin():
    def __init__(self, title):

        self.cwin = Toplevel()

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\ticket.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image
        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin)
        l = Label(tF, text="Welcome to buying ticket program")
        l.pack()


        bf3 = Frame(self.cwin)
        self.button_submit=Button(bf3, text ="BUY", width=10, command=self.tick)
        self.button_exit=Button(bf3, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT)
        self.button_exit.pack(side=RIGHT)
        
        tF.grid(row=1)
        bf3.grid(row=4,pady=10,padx=10)

        self.cwin.title(title)
        self.cwin.geometry('450x450')

    def tick(self):
        # do something
        calender()

class roomWin():
    def __init__(self, title):

        self.cwin = Toplevel()
        self.i = 1
        self.f = "filename"

        C = Canvas(self.cwin, bg="blue", height=50, width=50)

        filename1 = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\room0.png")

        #self.file = str(self.f)+str(self.i)
       
        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin,pady=15)


        b1 = Button(tF, text='<<', command=self.decre)
        b2 = Button(tF, text='>>', command=self.incre)

        b1.grid(row=1,column=0,rowspan=2)
        b2.grid(row=1,column=1)

        bf3 = Frame(self.cwin,pady=15)
        self.button_submit=Button(bf3, text ="BUY", width=10)
        self.button_exit=Button(bf3, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT)
        self.button_exit.pack(side=RIGHT)
        
        bf3.grid(row=2,column=0)
        tF.grid(row=1,column=0,padx=50)


        self.cwin.title(title)
        self.cwin.geometry('450x450')

    def incre(self):

        self.i = (self.i + 1) % 3

        s = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\room" + str(self.i) +".png"

        filename1 = PhotoImage(file = s)

        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)

    def decre(self):

        self.i = (self.i - 1) % 3

        s = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\room" + str(self.i) +".png" 

        filename1 = PhotoImage(file = s)

        background_label = Label(self.cwin, image=filename1)
        background_label.place(x=0, y=-100)

        background_label.image = filename1 # reference to the image
        background_label.grid(row=0,column=0)



#UserWindow()

