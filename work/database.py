import mysql.connector
from mysql.connector import Error
import datetime


class CustomerDB () :

    def __init__(self,cid,Fname,Lname,Phone,Email):
        self.cid = cid
        self.Fname = Fname
        self.Lname = Lname
        self.Phone = Phone
        self.Email = Email

    def queryuser(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            objdata = [self.cid ,self.Fname,self.Lname,self.Phone,self.Email]
            args = list() 
            sqlcmd = "select * from reserver where customer_ID = %s or Fname = %s or Lname = %s or Phone = %s or Email = %s" 
            for e in objdata:
                if e == "":
                    args.append(None)
                else : args.append(e)
            args = tuple(args)
            cursor = connection.cursor()
            cursor.execute(sqlcmd,args)
            reserverlist = cursor.fetchall()

            sqlcmd2 = "select * from guest where customer_ID = %s or Fname = %s or Lname = %s or Phone = %s or Email = %s" 
            cursor = connection.cursor()
            cursor.execute(sqlcmd2,args)
            guestlist = cursor.fetchall()

        except :
            retmsg = ["1","Error check some field"]
        
        else :
            retmsg = ["0",reserverlist,guestlist]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def usergetinfo(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            objdata = (self.Fname,self.Lname)

            sqlcmd = "select * from reserver where Fname = %s and Lname = %s " 
            cursor = connection.cursor()
            cursor.execute(sqlcmd,objdata)
            reserverlist = cursor.fetchall()

            sqlcmd2 = "select * from guest where Fname = %s and Lname = %s" 
            cursor = connection.cursor()
            cursor.execute(sqlcmd2,objdata)
            guestlist = cursor.fetchall()

        except :
            retmsg = ["1","Error check some field"]
        
        else :
            retmsg = ["0",reserverlist,guestlist]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg




                    







            
class staffDB():

    def __init__(self,SID,Fname,Lname,Sex,Salary,Address,Bdate,Age):
        self.SID = SID
        self.Fname = Fname
        self.Lname = Lname
        self.Sex = Sex
        self.Salary = Salary
        self.Address = Address
        self.Bdate = Bdate
        self.Age = Age
    
    def insertStaff(self):
        


        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
       
            objdata = (self.SID,  self.Fname , self.Lname,self.Sex,self.Salary ,\
                        self.Address , self.Bdate , self.Age)
            
            sqlQuery = "insert into "+"paradisepark.staff"+" (SID,Fname,Lname,Sex,Salary,Address,Bdate,Age) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            
            connection.commit()
            

        except:
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    
    def deleteBySID(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            objdata = (self.SID,)

            sqlQuery = "select * from "+"paradisepark.staff"+" where SID = %s"
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            del_data = records

            sqlQuery2 = "delete from "+"paradisepark.staff"+" where SID = %s"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2, objdata)


            connection.commit()
            
                    
        except:
            retmsg = ["1", "Delete Error"]
        else :
            if records == None :
                retmsg = ["0", "Staff with this SID is already not exist"]
            else : retmsg = ["0","Delete complete\n"+"Staff ID : "+del_data[0]+"\n"+"Name :"+del_data[1]+" "+del_data[2] ]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
            

    def deleteByName(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            objdata = (self.Fname,self.Lname,)

            sqlQuery = "select * from "+"paradisepark.staff"+" where Fname = %s and Lname = %s"
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchone()
            del_data = records

            sqlQuery2 = "delete from "+"paradisepark.staff"+" where Fname = %s and Lname = %s"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2, objdata)


            connection.commit()
            
                    
        except:
            retmsg = ["1", "Delete Error"]
        else :
            if records == None :
                retmsg = ["0", "Staff with this name is already not exist"]
            else : retmsg = ["0","Delete complete\n"+"Staff ID : "+del_data[0]+"\n"+"Name :"+del_data[1]+" "+del_data[2] ]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    
    def searchStaff(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            objdata = (self.SID,  self.Fname , self.Lname , self.Sex , self.Salary ,self.Address , self.Bdate , self.Age)
            newobj = list()
            for i in range(8):
                if objdata[i] == '' :
                    newobj.append(None)
                else : newobj.append(objdata[i])
            newobj = tuple(newobj)


            sqlQuery = "select * from paradisepark.staff where SID = %s or Fname = %s or Lname = %s or Sex = %s or Salary = %s or Address = %s or Bdate = %s or Age = %s"
            cursor = connection.cursor()
            cursor.execute(sqlQuery,newobj)
            records = cursor.fetchall()

        except:
            retmsg = ["1","Search Error"]
        else :
            retmsg = ["0",records]
        finally :
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

class playDB():

    def __init__(self,Rname,Fac,TA,cap,WarDu):
        self.Rname = Rname
        self.Fac = Fac 
        tI,tO = TA.split("-")
        self.tI = tI
        self.tO = tO
        self.cap = cap
        self.WarDu = WarDu
    
    def insertPlay(self):
        
        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
       
            objdata = (self.Rname,  self.Fac, self.tI,self.tO,self.cap ,self.WarDu)
            
            sqlQuery = "insert into "+"paradisepark.rides"+" (Rname,FacName,time_in,time_out,capacity,warrenty_duration) values (%s,%s,%s,%s,%s,%s)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            
            connection.commit()
            

        except:
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def deleteByRname(self) :

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            
            objData = (self.Rname,)

            sqlQuery = "select * from "+"paradisepark.rides"+" where Rname = %s "
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objData)
            records = cursor.fetchone()
            del_data = records
       
            sqlQuery2 = "delete from paradisepark.rides where Rname = %s"
            cursor= connection.cursor()
            cursor.execute(sqlQuery2,objData)

            connection.commit()


        except:
            retmsg = ["1","Delete Error"]
        else :
            if records == None :
                retmsg = ["0" , "This ride is already not found"]
            else : retmsg = ["0" , "Deleted\n Ride name :" +del_data[0]+"\n"]
        finally :
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def searchPlay(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            objdata = (self.Rname,  self.Fac, self.tI,self.tO,self.cap ,self.WarDu)
            newobj = list()
            for i in range(6):
                if objdata[i] == '' :
                    newobj.append(None)
                else : newobj.append(objdata[i])
            newobj = tuple(newobj)


            sqlQuery = "select * from paradisepark.rides where Rname = %s or FacName = %s or time_in = %s or time_out = %s or capacity = %s or warrenty_duration = %s "
            cursor = connection.cursor()
            cursor.execute(sqlQuery,newobj)
            records = cursor.fetchall()

        except:
            retmsg = ["1","Search Error"]
        else :
            retmsg = ["0",records]
        finally :
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def listAllPlay(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO




            sqlQuery = "select Rname , time_in , time_out from rides"
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            records = cursor.fetchall()

        except:
            retmsg = ["1","Search Error"]
        else :
            retmsg = ["0",records]
        finally :
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg


class ProductAndStoreDB():

    def __init__(self,Name,Price,Snum):

        self.Name = Name
        self.Price = Price
        self.Snum = Snum

    def insertProduct(self,Q):
        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            itemcmd = "insert into paradisepark.item (Item_Name,price) values (%s,%s)"
            productData = [self.Name , self.Price ]
            for i in range(Q-1):
                itemcmd += ", (%s,%s) "
                productData.append(self.Name)
                productData.append(self.Price)
            productData = tuple(productData)
            cursor = connection.cursor()
            cursor.execute(itemcmd,productData)
            connection.commit()

        except :
            retmsg = ["1","Error"] 
        
        else :
            retmsg = ["0", "Add Product Complete"]

        finally :
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def insertProductIntoStore(self,Q):
        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            productData = [self.Snum , 'F' ]
            itemcmd = "insert into paradisepark.sell_item (Snumber,has_sold) values (%s,%s)"
            for i in range(Q-1):
                itemcmd += ", (%s,%s) "
                productData.append(self.Snum)
                productData.append('F')
            productData = tuple(productData)
            cursor = connection.cursor()
            cursor.execute(itemcmd,productData)
            connection.commit()

        except :
            retmsg = ["1" , "Add Item Error"]
        
        else :
            retmsg = ["0", "Add to store no."+str(self.Snum)+"Complete"]

        finally :
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def updateProductPrice(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            
            objdata = (self.Name,)
            itemNamecmd = "select * from "+"paradisepark.item"+" where Item_Name = %s"
            cursor = connection.cursor()
            cursor.execute(itemNamecmd, objdata)
            records = cursor.fetchall()
            del_data = records

            itemList = [e[0] for e in del_data]
            l = len(itemList)
            sqlQuery2 = "update item set price = %s where Item_ID in ("
            for i in range(l):
                if i == l-1:
                    sqlQuery2 += "%s)"
                else : sqlQuery2 += "%s,"
            finalarg = tuple([self.Price] + itemList )
            cursor = connection.cursor()
            cursor.execute(sqlQuery2, finalarg)

            connection.commit()

        except :
            retmsg = ["1","Error"] 
        
        else :
            retmsg = ["0", "Update Product Price Complete"]
        finally :
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def deleteProductallStore(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            objdata = (self.Name,)

            sqlQuery = "select * from "+"paradisepark.item"+" where Item_Name = %s"
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchall()
            del_data = records

            itemList = tuple([e[0] for e in del_data])
            l = len(itemList)
            sqlQuery2 = "delete from "+"paradisepark.item"+" where Item_ID in ("
            for i in range(l):
                if i == l-1:
                    sqlQuery2 += "%s)"
                else : sqlQuery2 += "%s,"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2, itemList)

            connection.commit()

        except:
            retmsg = ["1","Error"]
        else :
            retmsg = ["0","delete complete"]
        finally :    
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    def QueryProduct(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO  

            objdata = (self.Name,)

            sqlQuery = "select Item_ID from "+"paradisepark.item"+" where Item_Name = %s"
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            records = cursor.fetchall()
            item_data = records


            itemList = tuple([e[0] for e in item_data])
            l = len(itemList)
            sqlQuery2 = "select SNumber from "+"paradisepark.sell_item"+" where Item_ID in ("
            for i in range(l):
                if i == l-1:
                    sqlQuery2 += "%s)"
                else : sqlQuery2 += "%s,"
            cursor = connection.cursor()
            cursor.execute(sqlQuery2, itemList)
            storenum = cursor.fetchall()

            storelist = tuple([e[0] for e in storenum])
            a = len(storelist)
            query3 = "select * from "+"paradisepark.slocation"+" where SNumber in ("
            for i in range(a):
                if i == a-1:
                    query3 += "%s)"
                else : query3+= "%s,"
            cursor = connection.cursor()
            cursor.execute(query3, storelist)
            ans = cursor.fetchall()

        except:
            retmsg = ["1","Error"]
        else :
            retmsg = ["0",ans]
        finally :    
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

            







class TickettypeDB():

    def __init__(self,typename,price):
        self.typename = typename
        self.price = price

    def updatePrice(self,newPrice):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            objdata = (newPrice,self.typename,)

            sqlQuery = "update ticket_price set price = %s where typename = %s "

            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
 

            connection.commit()

        except:
            retmsg = ["1","Error"]
        else :
            retmsg = ["0","update complete"]
        finally :    
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

class TicketDB():
    def __init__(self,sell_date,dname,typename,CID,year_sell,amount):
        self.sell_date = sell_date
        self.dname = dname
        self.typename = typename
        self.CID = CID
        self.year_sell = year_sell
        self.amount = amount

    def reserveTicket(self):
        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO  

            objdata = (self.sell_date,self.dname,self.typename,self.CID,self.year_sell,self.amount)

            sqlQuery = "insert into ticket (sell_date,Dname,typename,customer_ID,year_sell,amount) values (%s,%s,%s,%s,%s,%s)"

            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
 

            connection.commit()

            cursor = connection.cursor()
            querie = "select max(ticket_no) from ticket"
            cursor.execute(querie)
            rec = cursor.fetchone()


        except:
            retmsg = ["1","Error"]
        else :
            retmsg = ["0",rec]
        finally :    
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

class RoomDB():

    def __init__(self,room_no,Dname,billingID,r_type,phone,in_year,checkin_date,checkout_date):

        self.room_no = room_no
        self.Dname = Dname
        self.billingID = billingID
        self.r_type = r_type
        self.phone = phone
        self.in_year = in_year
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date

    def bookingRoom(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            objdata = (self.room_no,self.Dname,self.billingID,self.r_type ,self.phone,self.in_year,self.checkin_date,self.checkout_date)

            sqlQuery = "insert into room (room_no,Dname,billingID,r_type,phone,in_year,checkin_date,checkout_date) values (%s,%s,%s,%s,%s,%s,%s,%s)"

            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
 

            connection.commit()



        except:
            retmsg = ["1","Error"]
        else :
            retmsg = ["0","Booking Complete"]
        finally :    
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
class BillingDB():

    def __init__(self,customer_ID,creditcardNo,paymentDate):

        self.customer_ID = customer_ID
        self.creditcardNo = creditcardNo
        self.paymentDate = paymentDate
    
    def addBilling(self,BillingID):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO

            args = (self.customer_ID,BillingID,self.creditcardNo,self.paymentDate)
            sqlquery = "insert into billing (customer_ID,billingID,creditcard_no,payment_date) values (%s,%s,%s,%s)"
            cursor = connection.cursor()
            cursor.execute(sqlquery,args)

            connection.commit()



        except :
            retmsg = ["1","Error"]
        else :
            retmsg = ["0","Your billing ID is "+str(BillingID)+"\nuse it pay everything in accommodation"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg          




    def generateLatestBillID(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO


            cursor = connection.cursor()
            querie = "select max(billingID) from billing"
            cursor.execute(querie)
            rec = cursor.fetchone()

        except :
            return -1
        else :
            billID = int(rec[0]) + 1
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  billID          


class CheckBillingDB():

    def __init__(self,BillingID):

        self.BillingID = BillingID

    def getRoomBill(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO 


            arg = (self.BillingID,)
            querie = "select room_no , r_type , checkin_date , checkout_date from room where billingID = %s"
            cursor = connection.cursor()
            cursor.execute(querie,arg)
            rec = cursor.fetchall()


        except :
            retmsg = ['1' , "ERROR"]

        else :
            retmsg = ['0',rec]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg

    def getRoomPrice(self,rtype):
        
        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO 


            arg = (rtype,)
            querie = "select price_per_day  from roomtype where r_type = %s"
            cursor = connection.cursor()
            cursor.execute(querie,arg)
            rec = cursor.fetchone()

        except :
            retmsg = ['1' , "ERROR"]

        else :
            retmsg = ['0',rec]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg

    def getDinnerBill(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO 


            arg = (self.BillingID,)
            querie = "select dinner_date, total_price from include_food where billingID = %s"
            cursor = connection.cursor()
            cursor.execute(querie,arg)
            rec = cursor.fetchall()


        except :
            retmsg = ['1' , "ERROR"]

        else :
            retmsg = ['0',rec]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg

    def getFaBill(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO


            arg = (self.BillingID,)
            querie = "select FaName from include_service where billingID = %s"
            cursor = connection.cursor()
            cursor.execute(querie,arg)
            rec = cursor.fetchall()


        except :
            retmsg = ['1' , "ERROR"]

        else :
            retmsg = ['0',rec]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg        

    def getFaPrice(self,faname):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO


            arg = (faname,)
            querie = "select price from facility where FaName = %s"
            cursor = connection.cursor()
            cursor.execute(querie,arg)
            rec = cursor.fetchone()


        except :
            retmsg = ['1' , "ERROR"]

        else :
            retmsg = ['0',rec]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg  

    def getCusID(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO


            arg = (self.BillingID,)
            querie = "select customer_ID from billing where billingID = %s"
            cursor = connection.cursor()
            cursor.execute(querie,arg)
            rec = cursor.fetchone()


        except :
            retmsg = ['1' , "ERROR"]

        else :
            retmsg = ['0',rec]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg

    def getGuestInfo(self,cusID):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO 


            arg = (cusID,)
            querie = "select Fname , Lname ,phone,email from guest where customer_ID = %s"
            cursor = connection.cursor()
            cursor.execute(querie,arg)
            rec = cursor.fetchone()


        except :
            retmsg = ['1' , "ERROR"]

        else :
            retmsg = ['0',rec]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg

class incomeDB():

    def __init__(self,date):

        self.date = date

    def calculateTicket(self) :

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO             
            
            args = (self.date ,)
            queries = "select (amount * price) from ticket natural join ticket_price where sell_date = %s"

            cursor = connection.cursor()
            cursor.execute(queries,args)
            table = cursor.fetchall()
            ans = 0.0
            for e in table :
                ans += float(e[0])

        except :
            retmsg = ["1" , "Error"]

        else :
            retmsg = ["0" , ans]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg

    def calculateSellItem(self) :

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            
            
            arg = (self.date , )
            querie = "select price from item natural join sell_item where has_sold = 'T' and sell_date = %s"

            cursor = connection.cursor()
            cursor.execute(querie,arg)
            table = cursor.fetchall()
            ans = 0.0
            for e in table :
                ans += float(e[0])

        except :
            retmsg = ["1" , "Error"]

        else :
            retmsg = ["0" , ans]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg 

    def calculateRoonIncome(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            
            
            y,m,d = (self.date).split('-')
            x = datetime.date(int(y),int(m),int(d))
            querie = "select checkin_date , checkout_date ,price_per_day from room natural join roomtype "

            cursor = connection.cursor()
            cursor.execute(querie)
            table = cursor.fetchall()
            ans = 0.0
            for e in table :
                if e[0] <= x < e[1] :
                    ans += float(e[2])


        except :
            retmsg = ["1" , "Error"]

        else :
            retmsg = ["0" , ans]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg 

    def calculateDinnerIncome(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            
            
            dateobj = (self.date ,)
            querie = "select total_price from include_food where dinner_date = %s "

            cursor = connection.cursor()
            cursor.execute(querie,dateobj)
            table = cursor.fetchall()
            ans = 0.0
            for e in table :
                ans += float(e[0])




        except :
            retmsg = ["1" , "Error"]

        else :
            retmsg = ["0" , ans]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg 

    def calculateFaIncome(self):

        try:
            connection = mysql.connector.connect("""host='fill here',
                                                 database="paradisepark",
                                                 user="fill here",
                                                 password='fill here'""") #TODO
            
            
            dateobj = (self.date ,)
            querie = "SELECT price FROM facility natural join use_service where use_date = %s "

            cursor = connection.cursor()
            cursor.execute(querie,dateobj)
            table = cursor.fetchall()
            ans = 0.0
            for e in table :
                ans += float(e[0])




        except :
            retmsg = ["1" , "Error"]

        else :
            retmsg = ["0" , ans]

        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return  retmsg 