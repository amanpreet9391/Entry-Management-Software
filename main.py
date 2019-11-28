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
host=host()    #To get details of Host

mydb = connect_to_db()
mycursor = mydb.cursor()

while(True):
    print ("""
    Press 1 : Checkin           
    Press 2 : Checkout
    Press 3 : To export database into spreadsheet
    Press 4 : To exit """)

    status=int(input("Enter : "))
    if status==1:                   #If a visitor wants to Checkin
        
        visitor=visitors()          #Take details of Visitor
        V.append(visitor)
        mail_to_host(host,visitor)  #Mail to host about details of Visitor with checkin time
        sms_to_host(host,visitor)   # SMS to host about details of Visitor with checkin time
        
       
    elif status==2:                 # When a visitor wants to checkout
       
        id=input("Enter visitor's email address who wants to checkout : ")
        for i in V:
            if i[1]==id:
                
                checkout=timeStamp()
                i.append(checkout)
                mail_to_visitor(host,i)  # Mail to visitor about their detail with checkin and checkout time
                create_database(i)       # Make an entry for that visitor in the visitor's database 
                visitor_db(i)            # If you also want to make entry in a google spreadsheet(if you are creating a database in Excel sheets)
                
    elif status==3:    # If you want to export the whole database into a Excel sheet
        wb = Workbook()
        mycursor.execute("SELECT * FROM visitor")
        results = mycursor.fetchall()
        ws = wb.create_sheet(0)
       
        ws.append(mycursor.column_names)
        for row in results:
            ws.append(row)
        workbook_name = "test_workbook"
        wb.save(workbook_name + ".xlsx")


    elif status==4:                # When your work is done :)
        break










