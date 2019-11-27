import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456789"				#your mysql Password
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE db1")
mycursor.execute("use db1")
mycursor.execute("CREATE TABLE visitor ( Name TEXT, email VARCHAR(255),PhoneNumber VARCHAR(12) , CheckinDate TEXT ,CheckinTime TEXT, CheckoutDate TEXT, CheckoutTime TEXT)")
# wb = Workbook()
# mycursor.execute("SELECT * FROM visitor")
# results = mycursor.fetchall()
# ws = wb.create_sheet(0)
# #ws.title = visitor
# ws.append(mycursor.column_names)
# for row in results:
#     ws.append(row)
# workbook_name = "test_workbook"
# wb.save(workbook_name + ".xlsx")
