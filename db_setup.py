import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",              #your mysql user
  passwd="123456789"				#your mysql Password
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE db1")             # Create a database - db1
mycursor.execute("use db1")                         # Use that database to create a table inside it i.e. visitor
mycursor.execute("CREATE TABLE visitor ( Name TEXT, email VARCHAR(255),PhoneNumber VARCHAR(12) , CheckinDate TEXT ,CheckinTime TEXT, CheckoutDate TEXT, CheckoutTime TEXT)")
