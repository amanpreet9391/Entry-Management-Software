def host():
    host=[]
    print("Details of host")
    NameHost = input("Name : ")                     # Name of the Host
    host.append(NameHost)
    EmailHost = input("Email : ")                   # Email of the Host
    host.append(EmailHost)
    PhoneNoHost = input("Phone Number : ")          # Phone Number of the Host
    host.append(PhoneNoHost)
    Address = input("Address : ")                   # Address of the Host
    host.append(Address)
    return(host)