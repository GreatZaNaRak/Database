from tkinter import *
from PIL import Image, ImageTk 


class empIn():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\male2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0,pady=7)

        # body

        bf0 = Frame(self.cwin, pady=3)
        self.l0 = Label(bf0, text="SID: ")
        self.e0 = Entry(bf0)

        self.l1 = Label(bf0, text="SNumber: ")
        self.e1 = Entry(bf0)

        self.l0.grid(row=0,column=0,padx=10)
        self.e0.grid(row=0,column=1,padx=5)
        self.l1.grid(row=0,column=2)
        self.e1.grid(row=0,column=3)

        bf1 = Frame(self.cwin, pady=3)
        self.l2 = Label(bf1, text="FName: ")
        self.e2 = Entry(bf1)

        self.l3 = Label(bf1, text="LName: ")
        self.e3 = Entry(bf1)

        self.l2.grid(row=0,column=0,padx=10)
        self.e2.grid(row=0,column=1)
        self.l3.grid(row=0,column=2)
        self.e3.grid(row=0,column=3)

        bf2 = Frame(self.cwin, pady=3)
        self.l4 = Label(bf2, text="Sex: ")
        self.e4 = Entry(bf2)

        self.l5 = Label(bf2, text="Address: ")
        self.e5 = Entry(bf2)

        self.l4.grid(row=0,column=0,padx=10)
        self.e4.grid(row=0,column=1,padx=10)
        self.l5.grid(row=0,column=2)
        self.e5.grid(row=0,column=3)

        bf3 = Frame(self.cwin, pady=3)
        self.l6 = Label(bf3, text="Salary: ")
        self.e6 = Entry(bf3)

        self.l7 = Label(bf3, text="Bdate: ")
        self.e7 = Entry(bf3)

        self.l6.grid(row=0,column=0,padx=10)
        self.e6.grid(row=0,column=1,padx=10)
        self.l7.grid(row=0,column=2)
        self.e7.grid(row=0,column=3)
       
        bf4 = Frame(self.cwin, pady=3)
        self.l8 = Label(bf4, text="Age: ")
        self.e8 = Entry(bf4)

        self.l8.grid(row=0,column=0)
        self.e8.grid(row=0,column=1)


        bf5 = Frame(self.cwin, pady=10)

        self.but = Button(bf5, text="INSERT", width=15)
        self.exit = Button(bf5, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        bf0.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf4.grid(row=5)
        bf5.grid(row=6)


        self.cwin.title('Insert Employee')
        self.cwin.geometry('450x450')

class empOut():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\male2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Employee ID: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="Employee Name: ")
        self.empNameEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=10)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="DELETE", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Delete Employee')
        self.cwin.geometry('450x450')

class empQue():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\male2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0,pady=7)

        # body

        bf0 = Frame(self.cwin, pady=3)
        self.l0 = Label(bf0, text="SID: ")
        self.e0 = Entry(bf0)

        self.l1 = Label(bf0, text="SNumber: ")
        self.e1 = Entry(bf0)

        self.l0.grid(row=0,column=0,padx=10)
        self.e0.grid(row=0,column=1,padx=5)
        self.l1.grid(row=0,column=2)
        self.e1.grid(row=0,column=3)

        bf1 = Frame(self.cwin, pady=3)
        self.l2 = Label(bf1, text="FName: ")
        self.e2 = Entry(bf1)

        self.l3 = Label(bf1, text="LName: ")
        self.e3 = Entry(bf1)

        self.l2.grid(row=0,column=0,padx=10)
        self.e2.grid(row=0,column=1)
        self.l3.grid(row=0,column=2)
        self.e3.grid(row=0,column=3)

        bf2 = Frame(self.cwin, pady=3)
        self.l4 = Label(bf2, text="Sex: ")
        self.e4 = Entry(bf2)

        self.l5 = Label(bf2, text="Address: ")
        self.e5 = Entry(bf2)

        self.l4.grid(row=0,column=0,padx=10)
        self.e4.grid(row=0,column=1,padx=10)
        self.l5.grid(row=0,column=2)
        self.e5.grid(row=0,column=3)

        bf3 = Frame(self.cwin, pady=3)
        self.l6 = Label(bf3, text="Salary: ")
        self.e6 = Entry(bf3)

        self.l7 = Label(bf3, text="Bdate: ")
        self.e7 = Entry(bf3)

        self.l6.grid(row=0,column=0,padx=10)
        self.e6.grid(row=0,column=1,padx=10)
        self.l7.grid(row=0,column=2)
        self.e7.grid(row=0,column=3)
       
        bf4 = Frame(self.cwin, pady=3)
        self.l8 = Label(bf4, text="Age: ")
        self.e8 = Entry(bf4)

        self.l8.grid(row=0,column=0)
        self.e8.grid(row=0,column=1)


        bf5 = Frame(self.cwin, pady=10)

        self.but = Button(bf5, text="SEARCH", width=15)
        self.exit = Button(bf5, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        bf0.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf4.grid(row=5)
        bf5.grid(row=6)


        self.cwin.title('Query Employee')
        self.cwin.geometry('450x450')
