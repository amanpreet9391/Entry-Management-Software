from entry import timeStamp
from host import host
import os
import sys
import getpass
SECRET_FILE = "secret.txt"


def visitors():
    Visitor=[]
    print("Details of Visitor")
    with open(SECRET_FILE, "a") as f:
        #print("Enter your login: ")
        Name = input("Name : ")
    
        f.write(str(sys.stdin.readline().strip()) + ":")
        
        #print("Enter your login: ")
        Email = input("Email : ")
        f.write(str(sys.stdin.readline().strip()) + ":")
        
        #print("Enter your login: ")
        PhoneNo = input("Phone Number : ")
        f.write(str(sys.stdin.readline().strip()) + ":")
        
        #print("Enter your login: ")
        #f.write(str(sys.stdin.readline().strip()) + ":")
    
    Visitor.append(Name)
    Visitor.append(Email)
    
    Visitor.append(PhoneNo)
    #print(Name)
    #print(Email)
    #print(PhoneNo)
    Visitor.append(timeStamp())
    print(Visitor)
    return(Visitor)



visitors()
    