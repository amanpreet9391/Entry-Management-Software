#pip install twilio
# We need to sign up on twilio. After that we will generate a twilio phone number
#twilio phone number - +19384440616

import os
from twilio.rest import Client
account_sid = os.environ("TWILIO_ACCOUNT_SID")
auth_token = os.environ("TWILIO_AUTH_TOKEN")
