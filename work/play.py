from tkinter import *
from PIL import Image, ImageTk 


class pIn():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\p2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        
        bf1 = Frame(self.cwin,pady=5)
        self.l1 = Label(bf1, text="           Ride Name: ")
        self.e1 = Entry(bf1) 

        self.l1.pack(side=LEFT)
        self.e1.pack(side=RIGHT)

        bf2 = Frame(self.cwin,pady=5)
        self.l2 = Label(bf2, text="            Fac Name: ")
        self.e2 = Entry(bf2)

        self.l2.pack(side=LEFT)
        self.e2.pack(side=RIGHT)

        bf3 = Frame(self.cwin,pady=5)
        self.l3 = Label(bf3, text="     Time Available: ")
        self.e3 = Entry(bf3) 

        self.l3.pack(side=LEFT)
        self.e3.pack(side=RIGHT)

        bf4 = Frame(self.cwin,pady=5)
        self.l4 = Label(bf4, text="               Capacity: ")
        self.e4 = Entry(bf4)

        self.l4.pack(side=LEFT)
        self.e4.pack(side=RIGHT)

        bf5 = Frame(self.cwin,pady=5)
        self.l5 = Label(bf5, text="Warrant Duration: ")
        self.e5 = Entry(bf5)

        self.l5.pack(side=LEFT)
        self.e5.pack(side=RIGHT)


        bf6 = Frame(self.cwin,pady=5)
        self.button_submit=Button(bf6, text ="INSERT", width=10)
        self.button_exit=Button(bf6, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT,padx=10)
        self.button_exit.pack(side=RIGHT)

        
        bf1.grid(row=2,column=0)
        bf2.grid(row=3,column=0)
        bf3.grid(row=4,column=0)
        bf4.grid(row=5,column=0)
        bf5.grid(row=6,column=0)
        bf6.grid(row=7,column=0)


        self.cwin.title('Insert Plays')
        self.cwin.geometry('450x450')

class pOut():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\p2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.pID = Label(bdF, text="Plays ID: ")
        self.pEn = Entry(bdF)

        self.pName = Label(bdF, text="Plays Name: ")
        self.pNameEn = Entry(bdF)

        self.pID.grid(row=0,column=0)
        self.pEn.grid(row=0,column=1, pady=10)
        self.pName.grid(row=1,column=0)
        self.pNameEn.grid(row=1,column=1)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="DELETE", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Delete Plays')
        self.cwin.geometry('450x450')

class pQue():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\p2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        
        bf1 = Frame(self.cwin,pady=5)
        self.l1 = Label(bf1, text="           Ride Name: ")
        self.e1 = Entry(bf1) 

        self.l1.pack(side=LEFT)
        self.e1.pack(side=RIGHT)

        bf2 = Frame(self.cwin,pady=5)
        self.l2 = Label(bf2, text="            Fac Name: ")
        self.e2 = Entry(bf2)

        self.l2.pack(side=LEFT)
        self.e2.pack(side=RIGHT)

        bf3 = Frame(self.cwin,pady=5)
        self.l3 = Label(bf3, text="     Time Available: ")
        self.e3 = Entry(bf3) 

        self.l3.pack(side=LEFT)
        self.e3.pack(side=RIGHT)

        bf4 = Frame(self.cwin,pady=5)
        self.l4 = Label(bf4, text="               Capacity: ")
        self.e4 = Entry(bf4)

        self.l4.pack(side=LEFT)
        self.e4.pack(side=RIGHT)

        bf5 = Frame(self.cwin,pady=5)
        self.l5 = Label(bf5, text="Warrant Duration: ")
        self.e5 = Entry(bf5)

        self.l5.pack(side=LEFT)
        self.e5.pack(side=RIGHT)


        bf6 = Frame(self.cwin,pady=5)
        self.button_submit=Button(bf6, text ="SEARCH", width=10)
        self.button_exit=Button(bf6, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT,padx=10)
        self.button_exit.pack(side=RIGHT)

        bf1.grid(row=2,column=0)
        bf2.grid(row=3,column=0)
        bf3.grid(row=4,column=0)
        bf4.grid(row=5,column=0)
        bf5.grid(row=6,column=0)
        bf6.grid(row=7,column=0)


        self.cwin.title('Query Plays')
        self.cwin.geometry('450x450')
