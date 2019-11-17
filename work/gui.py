from tkinter import *
from emp import *
from play import *
from update import *
from product import *
from PIL import Image, ImageTk

class Window():
    def __init__(self):
        root = Tk()
        
        header = Label(root, text="Welcome Admin..")
        header.pack()

        # picture

        picFrame = Frame(root)

        img = Image.open('images\ddb.jpg')
        img = img.resize((450, 250), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(img)
        my_label = Label(picFrame, image=my_img)
        my_label.pack()

        picFrame.pack()

        # button

        bdFrame = Frame(root, pady=10)

        L = Label(bdFrame, text='Main Server running.. Please choose command')
        L.pack()

        r1 =Frame(bdFrame)

        insertButton = Button(r1, text="Insert", width=10, command=self.popSearch)
        insertButton.pack(side=LEFT, padx=5, pady=5)

        deleteButton = Button(r1, text='Delete', width=10, command=self.popDelete)
        deleteButton.pack(side=RIGHT)

        r2 = Frame(bdFrame)

        updateButton = Button(r2, text='Update', width=10, command=self.popUpdate)
        updateButton.pack(side=LEFT, padx=5)

        qButton = Button(r2, text='Query', width=10, command=self.popQuery)
        qButton.pack(side=RIGHT)
        

        r1.pack()
        r2.pack()
        bdFrame.pack()

        # footer

        fFrame = Frame(root)

        exitBut = Button(fFrame, text='exit', width=10, command=root.destroy)
        exitBut.pack(side=TOP)

        fFrame.pack()


        root.title("Databse GUI")
        root.geometry('450x450')
        root.mainloop()

    def popSearch(self):
        i = insertWin("Insertion Window")
    
    def popDelete(self):
        d = deleteWin("Deletion Window")
    
    def popUpdate(self):
        u = updateWin("Updating Window")
    
    def popQuery(self):
        q = queryWin("Query Window")

    def exit(self):
        exit()

class insertWin():
    def __init__(self, title):
        
        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\Get_mail.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin,pady=20)
        l = Label(tF, text="Select thing you want to insert...")
        l.pack()

        bf1 = Frame(self.cwin, pady=5)
        self.employBut = Button(bf1, text="EMPLOYEE", width=15, command=self.empIn)
        self.playBut = Button(bf1, text="PLAYS", width=15, command=self.pIn)

        self.employBut.pack(side=LEFT, padx=10)
        self.playBut.pack(side=RIGHT)

        bf2 = Frame(self.cwin, pady=5)
        self.productBut = Button(bf2, text="PRODUCT", width=15, command=self.prIn)
        self.exitBut = Button(bf2, text="EXIT", width=15, command=self.cwin.destroy)

        self.productBut.pack(side=LEFT, padx=10)
        self.exitBut.pack(side=RIGHT)

        tF.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
       

        self.cwin.title(title)
        self.cwin.geometry('450x450')

    def empIn(self):
        empIn()
    
    def pIn(self):
        pIn()
    
    def prIn(self):
        prIn()

class deleteWin():
    def __init__(self, title):
        
        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\bin.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin,pady=20)
        l = Label(tF, text="Select thing you want to delete...")
        l.pack()

        bf1 = Frame(self.cwin, pady=5)
        self.employBut = Button(bf1, text="EMPLOYEE", width=15,command=self.empOut)
        self.playBut = Button(bf1, text="PLAYS", width=15, command=self.pOut)

        self.employBut.pack(side=LEFT, padx=10)
        self.playBut.pack(side=RIGHT)

        bf2 = Frame(self.cwin, pady=5)
        self.productBut = Button(bf2, text="PRODUCT", width=15, command=self.prOut)
        self.exitBut = Button(bf2, text="EXIT", width=15, command=self.cwin.destroy)

        self.productBut.pack(side=LEFT, padx=10)
        self.exitBut.pack(side=RIGHT)

        tF.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
       

        self.cwin.title(title)
        self.cwin.geometry('450x450')

    def empOut(self):
        empOut() 
    
    def pOut(self):
        pOut()
    
    def prOut(self):
        prOut()

    

class updateWin():
    def __init__(self, title):
        
        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\update.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin, pady=20)
        l = Label(tF, text="Select thing you want to update...")
        l.pack()

        bf1 = Frame(self.cwin, pady=5)
        self.tickPriceBut = Button(bf1, text="TICKET PRICE", width=15, command=self.upTic)
        self.playPriceBut = Button(bf1, text="PLAYS PRICE", width=15, command=self.upPlay)

        self.tickPriceBut.pack(side=LEFT, padx=10)
        self.playPriceBut.pack(side=RIGHT)

        bf2 = Frame(self.cwin, pady=5)
        self.exBut = Button(bf2, text="EXIT", width=15, command=self.cwin.destroy)
        
        self.exBut.pack()
        
        tF.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        

        self.cwin.title(title)
        self.cwin.geometry('450x450')
    
    def upTic(self):
        upTicket()
    
    def upPlay(self):
        upPlay()

        


class queryWin():
    def __init__(self, title):
        
        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\qu.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin)
        l = Label(tF, text="Select thing you want to query..")
        l.pack()

        bf1 = Frame(self.cwin,pady=5)
        self.empBut = Button(bf1, text="EMPLOYEE", width=15,command=self.empQ)
        self.userBut = Button(bf1, text="USER", width=15)

        self.empBut.pack(side=LEFT,padx=10)
        self.userBut.pack(side=RIGHT)

        bf2 = Frame(self.cwin,pady=5)
        self.playBut = Button(bf2, text="PLAYS", width=15, command=self.pQ)
        self.billBut = Button(bf2, text="PRODUCT", width=15, command=self.prQ)

        self.playBut.pack(side=LEFT,padx=10)
        self.billBut.pack(side=RIGHT)

        bf3 = Frame(self.cwin,pady=5)
        self.roomBut = Button(bf3, text ="ROOMER", width=15)
        self.inBut = Button(bf3, text="INCOME", width=15)

        self.roomBut.pack(side=LEFT,padx=10)
        self.inBut.pack(side=RIGHT)

        bf4 = Frame(self.cwin,pady=5)
        self.ex = Button(bf4, text ="EXIT", width=15, command=self.cwin.destroy)
        self.ex.pack()
        
        tF.grid(row=1)
        bf1.grid(row=2)
        bf2.grid(row=3)
        bf3.grid(row=4)
        bf4.grid(row=5)
 
       

        self.cwin.title(title)
        self.cwin.geometry('450x450')
    
    def empQ(self):
        empQue()
    
    def pQ(self):
        pQue()

    def prQ(self):
        prQ()
        




Window()