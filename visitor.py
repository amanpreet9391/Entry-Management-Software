from entry import timeStamp
from host import host

def visitors():
    Visitor=[]
    print("Details of Visitor")
    Name = input("Name : ")
    Visitor.append(Name)
    Email = input("Email : ")
    Visitor.append(Email)
    PhoneNo = input("Phone Number : ")
    Visitor.append(PhoneNo)
    #print(Name)
    #print(Email)
    #print(PhoneNo)
    #Visitor.append(timeStamp())
    time=timeStamp()
    Visitor.append(time)
    #print(Visitor)
    return(Visitor)
