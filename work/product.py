from tkinter import *
from database import *
from PIL import Image, ImageTk 


class prIn():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\pr.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Product Name: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="Product Price: ")
        self.empNameEn = Entry(bdF)

        self.empAge = Label(bdF, text="Product Quantity: ")
        self.empAgeEn = Entry(bdF)

        self.empSta = Label(bdF, text="Add to Store number: ")
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

        self.but = Button(foot, text="INSERT", width=15,command=self.addPr)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        moreFoot = Frame(self.cwin)

        self.label_status = Label(moreFoot,text="please add all the field")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        foot.grid(row=2)
        moreFoot.grid(row = 3)


        self.cwin.title('Insert Product into store')
        self.cwin.geometry('450x600')

    def addPr(self):

        self.cwin.title("Added")
        Name = self.empEn.get()
        price = self.empNameEn.get()
        quantity = self.empAgeEn.get()
        Snum = self.empStaEn.get()
        anAdding = ProductAndStoreDB(Name,price,Snum)
        retmsg1 =  anAdding.insertProduct(int(quantity))
        retmsg2 = anAdding.insertProductIntoStore(int(quantity))
        retmsg = retmsg1[1] + "\n" + retmsg2[1]
        self.label_status.config(text=retmsg)




class prOut():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\pr.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Product Name: ")
        self.empEn = Entry(bdF)


        self.empID.grid(row=1,column=0)
        self.empEn.grid(row=1,column=1, pady=10)


        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="DELETE", width=15,command=self.delProduct)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)
        
        morefoot = Frame(self.cwin)
        self.label_status = Label(morefoot,text="Please fill product name ")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        foot.grid(row=2)
        morefoot.grid(row=3)





        self.cwin.title('Delete Product all Store')
        self.cwin.geometry('450x600')

    def delProduct(self):

        self.cwin.title('Deleted')
        name = self.empEn.get()
        anP = ProductAndStoreDB(name,"0.00",'0')
        retmsg = anP.deleteProductallStore()
        self.label_status.config(text=retmsg[1])


class prQ():

    def __init__(self):
    
        self.cwin = Toplevel()

        # head
        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "images\\pr.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Product Name: ")
        self.empEn = Entry(bdF)


        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=5)
 

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)


        self.but = Button(foot, text="SEARCH", width=15,command=self.QueryP)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        moreFoot = Frame(self.cwin)
        self.label_status = Label(moreFoot,text="fill Product name")

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)
        self.label_status.pack()

        foot.grid(row=2)
        moreFoot.grid(row=3)


        self.cwin.title('Query Product')
        self.cwin.geometry('450x600')

    def QueryP(self):

        self.cwin.title('Complete')
        name = self.empEn.get()
        anP = ProductAndStoreDB(name,"0.00",'0')
        retmsg = anP.QueryProduct()
        show = ""
        for e in retmsg[1] :
            if len(e) != 0 and retmsg[0] != "1" :
                show += "Sell at Store no.: " + str(e[0]) + "\n" + "Location : "+str(e[1]) + "\n" 
        if show == "" : show = " sorry,It not sell in our store"
        self.label_status.config(text=show)
