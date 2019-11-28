import boto3
import json



def sms_to_host(host,Visitor):
    # Create an SNS client
    with open('creds.json') as data_file:        # creds.json is the file which contains accesskey and secret access key id
        data = json.load(data_file)


        
        client = boto3.client(
            "sns",
            aws_access_key_id = data['aws_access_key_id'],
            aws_secret_access_key =  data['aws_secret_access_key'],
            
            region_name="us-east-1"
    )

    # Send your sms message.
    client.publish(
        PhoneNumber="+91" + host[2],
        Message= "Name - " + Visitor[0] + "\n" + "Email - " + Visitor[1] + "\n" + "Phone Number - " + Visitor[2] + "\n" + "Checkin Time - " + Visitor[3][1]
    )
    print("Message Delivered")


