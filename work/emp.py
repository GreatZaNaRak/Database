from tkinter import *
from PIL import Image, ImageTk 
from database import *


class empIn():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\male2.png")
       
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

        #add msg
        bf6 = Frame(self.cwin,pady=3)
        self.label_status = Label(bf6, text="haha see it?")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        bf0.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf4.grid(row=5)
        bf5.grid(row=6)

        bf6.grid(row=7,columnspan=2)


        self.cwin.title('Insert Employee')
        self.cwin.geometry('450x600')
        self.but.configure(text="INSERT", command=self.insertEmp)

    def insertEmp(self):
        self.cwin.title("Inserted")
        SID = self.e0.get()
        Fname = self.e2.get()
        Lname = self.e3.get()
        Sex = self.e4.get()
        Salary = self.e6.get()
        Address = self.e5.get()
        Bdate = self.e7.get()
        Age = self.e8.get()
        anEmployee = staffDB(SID,Fname,Lname,Sex,Salary,Address,Bdate,Age)
        retmsg = anEmployee.insertStaff()
        self.label_status.config(text=retmsg[1])


class empOut():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\male2.png")
       
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

        self.but = Button(foot, text="DELETE", width=15,command= self.delEmp)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)

        #add return massage
        morefoot = Frame(self.cwin)

        self.label_status = Label(morefoot, text="you can remove staff from database\nby 'SID' or 'firstname lastname'")
        self.label_status.pack()

        morefoot.grid(row=3)



        self.cwin.title('Delete Employee')
        self.cwin.geometry('450x600')
    
    def delEmp(self):

        self.cwin.title("Deleted")
        delID = self.empEn.get()
        delName = self.empNameEn.get()
        print(delName)
        anEmployee = staffDB(delID,delName,None,None,None,None,None,None)
        if delID != None :
            retmsg = anEmployee.deleteBySID()
            self.label_status.config(text=retmsg[1])
        if delName != None :
            name , surname = delName.split()
            anEmployee = staffDB(None,name,surname,None,None,None,None,None)
            retmsg = anEmployee.deleteByName()
            self.label_status.config(text=retmsg[1])

        


class empQue():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\male2.png")
       
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

        self.but = Button(bf5, text="SEARCH", width=15,command=self.searchEmp)
        self.exit = Button(bf5, text="EXIT", width=15, command=self.cwin.destroy)

        bf6 = Frame(self.cwin,pady=3)
        self.label_status = Label(bf6, text="fill what you want to know. , we will list first 3 of them")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        bf0.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf4.grid(row=5)
        bf5.grid(row=6)
        bf6.grid(row=7)


        self.cwin.title('Query Employee')
        self.cwin.geometry('450x800')

    def searchEmp(self):

        self.cwin.title("Result")
        SID = self.e0.get()
        Fname = self.e2.get()
        Lname = self.e3.get()
        Sex = self.e4.get()
        Salary = self.e6.get()
        Address = self.e5.get()
        Bdate = self.e7.get()
        Age = self.e8.get()
        anEmployee = staffDB(SID,Fname,Lname,Sex,Salary,Address,Bdate,Age)
        retmsg = anEmployee.searchStaff()
        txt = "Not found" ; c = 0
        for e in retmsg[1]:
            if c == 0 : txt = "" 
            if c == 3 : break
            txt += "SID : "+ str(e[0])+"\n" + \
                    "Name :"+ str(e[1])+" "+str(e[2])+"\n"+ \
                    "Sex :" + ("Male" if e[3] == 'M' else "Female") + "\n"+\
                    "Salary : "+ str(e[4])+" THB" + "\n" +\
                    "Address: "+str(e[5]) + "\n" +\
                    "Birthdate :" + str(e[6]) + "  Age : " + str(e[7]) +" years"+"\n   *********   \n"
            c+=1
        self.label_status.config(text=txt)

