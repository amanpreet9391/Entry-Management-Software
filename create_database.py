import mysql.connector
def create_database(visitor):
    query = "INSERT INTO visitor (Name,email,PhoneNumber,CheckinDate, CheckinTime,CheckoutDate, CheckoutTime) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (visitor[0],visitor[1],visitor[2],visitor[3][0],visitor[3][1],visitor[4][0],visitor[4][1])
    mycursor.execute(query,values)
    mydb.commit()