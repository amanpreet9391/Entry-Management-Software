#pip install twilio
# We need to sign up on twilio. After that we will generate a twilio phone number
#twilio phone number - +19384440616

import os
from twilio.rest import Client
account_sid = 'AC2b3e6fb54dabcfac887167d0868cfa7e'
auth_token = '69689f699943c4b46c6f86ef4d519e53'

  
# Your Account Sid and Auth Token from twilio.com / console 

  
client = Client(account_sid, auth_token) 
  
''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
message = client.messages.create( 
                              from_='+19384440616', 
                              body ='body', 
                              to ='+918003030099'
                          ) 
  
print(message.sid) 