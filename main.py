from host import host
from visitor import visitors
from entry import timeStamp
from mail import mail_to_host
from mail import mail_to_visitor
from sns import sms_to_host
from create_visitor_database import create_database
from create_visitor_database import connect_to_db
from visitor_db import visitor_db
import mysql.connector
from openpyxl import Workbook

V=[]
id=0
host=host()
# def connect_to_db():
#     mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "123456789",
#     database = "db1"
#     )
#     return mydb
    

mydb = connect_to_db()
mycursor = mydb.cursor()





# def create_database(visitor):
#     query = "INSERT INTO visitor (Name,email,PhoneNumber,CheckinDate, CheckinTime,CheckoutDate, CheckoutTime) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#     values = (visitor[0],visitor[1],visitor[2],visitor[3][0],visitor[3][1],visitor[4][0],visitor[4][1])
#     mycursor.execute(query,values)
#     mydb.commit()
while(True):
    print ("""
    Press 1 : Checkin
    Press 2 : Checkout
    Press 3 : To export database into spreadsheet
    Press 4 : To exit """)

    status=int(input("Enter : "))
    if status==1:
        
        visitor=visitors()
        V.append(visitor)
        # mail_to_host(host,visitor)
        # sms_to_host(host,visitor)
        
       



    elif status==2:
       
        id=input("Enter visitor's email address who wants to checkout : ")
        for i in V:
            if i[1]==id:
                #print(i)
                checkout=timeStamp()
                i.append(checkout)
                #mail_to_visitor(host,i)
                
                #print(i)
                create_database(i)

                visitor_db(i)
                
    elif status==3:
        wb = Workbook()
        mycursor.execute("SELECT * FROM visitor")
        results = mycursor.fetchall()
        ws = wb.create_sheet(0)
        #ws.title = visitor
        ws.append(mycursor.column_names)
        for row in results:
            ws.append(row)
        workbook_name = "test_workbook"
        wb.save(workbook_name + ".xlsx")







    elif status==4:
        break










