from tkinter import *
from PIL import Image, ImageTk 


class prIn():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\pr.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Product ID: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="Product Name: ")
        self.empNameEn = Entry(bdF)

        self.empAge = Label(bdF, text="Product Price: ")
        self.empAgeEn = Entry(bdF)

        self.empSta = Label(bdF, text="Product Status: ")
        self.empStaEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=5)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1,pady=5)
        self.empAge.grid(row=2,column=0)
        self.empAgeEn.grid(row=2,column=1,pady=5)
        self.empSta.grid(row=3,column=0)
        self.empStaEn.grid(row=3,column=1,pady=5)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="INSERT", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Insert Product')
        self.cwin.geometry('450x450')

class prOut():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\pr.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Product ID: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="Product Name: ")
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


        self.cwin.title('Delete Product')
        self.cwin.geometry('450x450')

class prQ():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\pr.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Product ID: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="Product Name: ")
        self.empNameEn = Entry(bdF)

        self.empAge = Label(bdF, text="Product Price: ")
        self.empAgeEn = Entry(bdF)

        self.empSta = Label(bdF, text="Product Status: ")
        self.empStaEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=5)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1,pady=5)
        self.empAge.grid(row=2,column=0)
        self.empAgeEn.grid(row=2,column=1,pady=5)
        self.empSta.grid(row=3,column=0)
        self.empStaEn.grid(row=3,column=1,pady=5)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="SEARCH", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Query Product')
        self.cwin.geometry('450x450')
