from tkinter import *
from database import *
from PIL import Image, ImageTk 


class pIn():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\p2.png")
       
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
        self.l3 = Label(bf3, text="Time Available:\n('hh:mm:ss'-'hh:mm:ss')")
        self.e3 = Entry(bf3) 

        self.l3.pack(side=LEFT)
        self.e3.pack(side=RIGHT)

        bf4 = Frame(self.cwin,pady=5)
        self.l4 = Label(bf4, text="               Capacity: ")
        self.e4 = Entry(bf4)

        self.l4.pack(side=LEFT)
        self.e4.pack(side=RIGHT)

        bf5 = Frame(self.cwin,pady=5)
        self.l5 = Label(bf5, text="Warrant Duration(years): ")
        self.e5 = Entry(bf5)

        self.l5.pack(side=LEFT)
        self.e5.pack(side=RIGHT)


        bf6 = Frame(self.cwin,pady=5)
        self.button_submit=Button(bf6, text ="INSERT", width=10,command=self.insertP)
        self.button_exit=Button(bf6, text="EXIT", width=10, command=self.cwin.destroy)

        bf7 = Frame(self.cwin)
        self.label_status = Label(bf7, text="haha see it?")

        self.button_submit.pack(side=LEFT,padx=10)
        self.button_exit.pack(side=RIGHT)
        self.label_status.pack()

        
        bf1.grid(row=2,column=0)
        bf2.grid(row=3,column=0)
        bf3.grid(row=4,column=0)
        bf4.grid(row=5,column=0)
        bf5.grid(row=6,column=0)
        bf6.grid(row=7,column=0)
        bf7.grid(row=8,columnspan=2)


        self.cwin.title('Insert Plays')
        self.cwin.geometry('450x600')
    
    def insertP(self):
        self.cwin.title('Inserted')
        Rname = self.e1.get()
        Fac = self.e2.get()
        TA = self.e3.get()
        Cap = self.e4.get()
        WarDu = self.e5.get()
        aPlay = playDB(Rname,Fac,TA,Cap,WarDu)
        retmsg = aPlay.insertPlay()
        self.label_status.config(text=retmsg[1])

class pOut():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\p2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)


        self.pName = Label(bdF, text="Plays Name: ")
        self.pNameEn = Entry(bdF)

        self.pName.grid(row=0,column=0)
        self.pNameEn.grid(row=0,column=1,pady=10)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="DELETE", width=15,command=self.delP)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        moreFoot = Frame(self.cwin)
        self.label_status = Label(moreFoot,text="add ride name that you want to delete.")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        foot.grid(row=2)
        moreFoot.grid(row=3)


        self.cwin.title('Delete Plays')
        self.cwin.geometry('450x600')

    def delP(self):
        Rname = self.pNameEn.get()
        aPlay = playDB(Rname,None,"Unknown-Unknown",None,None)
        retmsg = aPlay.deleteByRname()
        self.label_status.config(text=retmsg[1])

class pQue():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\p2.png")
       
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
        self.button_submit=Button(bf6, text ="SEARCH", width=10,command=self.searchP)
        self.button_exit=Button(bf6, text="EXIT", width=10, command=self.cwin.destroy)

        bf7 = Frame(self.cwin)
        self.label_status = Label(bf7,text="fill what you want to know. , we will list first 3 of them")

        self.button_submit.pack(side=LEFT,padx=10)
        self.button_exit.pack(side=RIGHT)
        self.label_status.pack()

        bf1.grid(row=2,column=0)
        bf2.grid(row=3,column=0)
        bf3.grid(row=4,column=0)
        bf4.grid(row=5,column=0)
        bf5.grid(row=6,column=0)
        bf6.grid(row=7,column=0)
        bf7.grid(row=8,columnspan=2)


        self.cwin.title('Query Plays')
        self.cwin.geometry('450x700')
    
    def searchP(self):

        self.cwin.title("Searched")
        Rname = self.e1.get()
        Fac = self.e2.get()
        e3tmp = self.e3.get()
        if "-" not in e3tmp  :
            TA = "-"
        else : TA = e3tmp
        Cap = self.e4.get()
        WarDu = self.e5.get()
        aPlay = playDB(Rname,Fac,TA,Cap,WarDu)
        retmsg = aPlay.searchPlay()
        txt = "Not found" ; c = 0
        for e in retmsg[1]:
            if c == 0 : txt = "" 
            if c == 3 : break
            txt += "Ride Name : "+ str(e[0])+"\n" + \
                    "Manufacturer :"+ str(e[1])+"\n"+ \
                    "Available Time :" + str(e[2])+ " - "+str(e[3]) + "\n"+\
                    "Capacity : "+ str(e[4]) + "\n" +\
                    "Warrenty Year(s): "+str(e[5]) +" year(s)"+"\n   *********   \n"
            c+=1
        self.label_status.config(text=txt)
        
