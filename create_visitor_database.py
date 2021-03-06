import mysql.connector

def connect_to_db():                        # Connect to our database i.e. db1
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456789",
    database = "db1"
    )
    return mydb
    

mydb = connect_to_db()
mycursor = mydb.cursor()

def create_database(visitor):         # Insert into database- db1 and a table inside it for visitors 
    query = "INSERT INTO visitor (Name,email,PhoneNumber,CheckinDate, CheckinTime,CheckoutDate, CheckoutTime) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (visitor[0],visitor[1],visitor[2],visitor[3][0],visitor[3][1],visitor[4][0],visitor[4][1])
    mycursor.execute(query,values)
    mydb.commit()

