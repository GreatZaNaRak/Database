from tkinter import *
#from database import *
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

        tF = Frame(self.cwin)
        l = Label(tF, text="Inserting Data...")
        l.pack()

        bf1 = Frame(self.cwin)
        self.label_id=Label(bf1, text="UserID = ")
        self.entry_id=Entry(bf1)

        self.label_id.pack(side=LEFT)
        self.entry_id.pack(side=RIGHT)

        bf2 = Frame(self.cwin)
        self.label_name=Label(bf2, text="Values = ")
        self.entry_name=Entry(bf2)

        self.label_name.pack(side=LEFT)
        self.entry_name.pack(side=RIGHT)

        bf3 = Frame(self.cwin)
        self.button_submit=Button(bf3, text ="INSERT", width=10, command=self.searchCustomer)
        self.button_exit=Button(bf3, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT)
        self.button_exit.pack(side=RIGHT)
        
        tF.grid(row=1)
        bf1.grid(row=2,pady=10,padx=5)
        bf2.grid(row=3,pady=10)
        bf3.grid(row=4,pady=10,padx=10)
 
       

        self.cwin.title(title)
        self.cwin.geometry('450x450')

        

    def searchCustomer(self):
      
        self.cwin.title("Searched")
        dataentry = [self.entry_id.get(), self.entry_name.get()]
        #aCustomer = Customer(dataentry)
        
        #retmsg = aCustomer.search()

        #if retmsg[0] == "0" :
        #    self.entry_id.delete(0, END)
        #    self.entry_id.insert(0, aCustomer.getInfo()[0])
        #    self.entry_name.delete(0, END)
        #    self.entry_name.insert(0, aCustomer.getInfo()[1])
            
        #else :
        #    self.entry_name.delete(0, END)
        #    self.entry_name.insert(0, "?????")
        #self.label_status.config(text=retmsg[1])    

class deleteWin():
    def __init__(self, title):
        
        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\bin.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin)
        l = Label(tF, text="Deleting Data...")
        l.pack()

        bf1 = Frame(self.cwin)
        self.label_id=Label(bf1, text="UserID = ")
        self.entry_id=Entry(bf1)

        self.label_id.pack(side=LEFT)
        self.entry_id.pack(side=RIGHT)

        bf2 = Frame(self.cwin)
        self.label_name=Label(bf2, text="Name = ")
        self.entry_name=Entry(bf2)

        self.label_name.pack(side=LEFT)
        self.entry_name.pack(side=RIGHT)

        bf3 = Frame(self.cwin)
        self.button_submit=Button(bf3, text ="DELETE", width=10)
        self.button_exit=Button(bf3, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT)
        self.button_exit.pack(side=RIGHT)
        
        tF.grid(row=1)
        bf1.grid(row=2,pady=10,padx=5)
        bf2.grid(row=3,pady=10)
        bf3.grid(row=4,pady=10,padx=10)
 
       

        self.cwin.title(title)
        self.cwin.geometry('450x450')

        

    

class updateWin():
    def __init__(self, title):
        
        self.cwin = Toplevel()

        
        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\update.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        tF = Frame(self.cwin)
        l = Label(tF, text="Updating Data...")
        l.pack()

        bf1 = Frame(self.cwin)
        self.label_id=Label(bf1, text="UserID = ")
        self.entry_id=Entry(bf1)

        self.label_id.pack(side=LEFT)
        self.entry_id.pack(side=RIGHT)

        bf2 = Frame(self.cwin)
        self.label_name=Label(bf2, text="Name = ")
        self.entry_name=Entry(bf2)

        self.label_name.pack(side=LEFT)
        self.entry_name.pack(side=RIGHT)

        bf3 = Frame(self.cwin)
        self.button_submit=Button(bf3, text ="UPDATE", width=10)
        self.button_exit=Button(bf3, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT)
        self.button_exit.pack(side=RIGHT)
        
        tF.grid(row=1)
        bf1.grid(row=2,pady=10,padx=5)
        bf2.grid(row=3,pady=10)
        bf3.grid(row=4,pady=10,padx=10)
 
       

        self.cwin.title(title)
        self.cwin.geometry('450x450')

        


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
        l = Label(tF, text="Quering Data...")
        l.pack()

        bf1 = Frame(self.cwin)
        self.label_id=Label(bf1, text="Command = ")
        self.entry_id=Entry(bf1)

        self.label_id.pack(side=LEFT)
        self.entry_id.pack(side=RIGHT)

        bf2 = Frame(self.cwin)
        self.label_name=Label(bf2, text="Result = ")
        self.entry_name=Entry(bf2)

        self.label_name.pack(side=LEFT)
        self.entry_name.pack(side=RIGHT)

        bf3 = Frame(self.cwin)
        self.button_submit=Button(bf3, text ="ASK", width=10)
        self.button_exit=Button(bf3, text="EXIT", width=10, command=self.cwin.destroy)

        self.button_submit.pack(side=LEFT)
        self.button_exit.pack(side=RIGHT)
        
        tF.grid(row=1)
        bf1.grid(row=2,pady=10,padx=5)
        bf2.grid(row=3,pady=10)
        bf3.grid(row=4,pady=10,padx=10)
 
       

        self.cwin.title(title)
        self.cwin.geometry('450x450')

        




#Window()