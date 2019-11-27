import json

with open('creds.json') as data_file:
    data = json.load(data_file)


aws_access_key_id = data['aws_access_key_id']
aws_secret_access_key =  data['aws_secret_access_key']

#print(aws_access_key_id)
