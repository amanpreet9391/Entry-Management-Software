from entry import timeStamp
from host import host

def visitors():
    Visitor=[]
    print("Details of Visitor")
    Name = input("Name : ")                         # Name of Visitor
    Visitor.append(Name)
    Email = input("Email : ")                       # Email id of Visitor
    Visitor.append(Email)
    PhoneNo = input("Phone Number : ")              # Phone Number of Visitor
    Visitor.append(PhoneNo)
    time=timeStamp()
    Visitor.append(time)
    return(Visitor)
