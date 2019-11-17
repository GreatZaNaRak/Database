import mysql.connector
from mysql.connector import Error


class Customer():
    def __init__(self, data):
        self.custDataObj = CustomerDB(data)
    
    def search(self):
        return self.custDataObj.searchDB('test', 'student')

    def write(self):
        return self.custDataObj.writeDB('test', 'student')

    def getInfo(self):
        return self.custDataObj.data


class CustomerDB():

    def __init__(self, data):
        self.data = data

    def writeDB(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password='')
       
            objdata = (wdata[0], wdata[1])
            
            sqlQuery = "insert into "+table+" (id, name) " \
                               "values (%s,%s)"
            
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

    
    def searchDB(self, databasename, table):

        key = str(self.data[0])

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database=databasename,
                user='root',
                password=''
            )

            objData = (key,)
            command = 'select * from '+table+' where id = %s'
            
            cursor = connection.cursor()
            cursor.execute(command, objData)

            rec = cursor.fetchone()
            self.data = rec
            
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if rec[1] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
            
