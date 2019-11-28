import smtplib
import getpass
def mail_to_host(host,Visitor):						#function for sending mail to host
	
    
    content1= "Name - " + Visitor[0] + "\n" + "Email - " + Visitor[1] + "\n" + "Phone Number - " + Visitor[2] + "\n" + "Checkin Time - " + Visitor[3][1]
	
    mail=smtplib.SMTP('smtp.gmail.com',587 )				#smtp mail id and port number
    mail.ehlo()
    mail.starttls()
    sender_email=input("Enter email address of sender : ")
    sender_password=getpass.getpass("Enter password : ")	     
    mail.login(sender_email,sender_password)	
    mail.sendmail(sender_email,host[1],content1)       #(sender'mail id,receiver's mail id,content)
	
	
    mail.close()
    print("mail delivered")


def mail_to_visitor(host,Visitor):						#function for sending mail to visitor
	
   
    
    content1= "Name - " + Visitor[0] + "\n" + "Phone Number - " + Visitor[2] + "\n" + "Checkin Time - " + Visitor[3][1] + "\n" + "CheckOut Time - " + Visitor[4][1] + "\n" + "Host Name - " + host[0] + "\n" + "Address Visited - " + host[3]
	
    mail=smtplib.SMTP('smtp.gmail.com',587 )				#smtp mail id and port number
    mail.ehlo()
    mail.starttls()
    
    sender_email=input("Enter email address of sender : ")
    sender_password=getpass.getpass("Enter password for sender's id : ")
			     
    mail.login(sender_email,sender_password)	
    mail.sendmail(sender_email,Visitor[1],content1)       #(sender'mail id,receiver's mail id,content)
	
	
    mail.close()
    print("mail delivered")