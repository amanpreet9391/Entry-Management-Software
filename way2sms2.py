import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'
apiKey = 'ZAVU0S7QF07BR90BKCC5RJ8IVDOFKLCI'
secretKey = '1U6VPIR91LQZDH93'
#useType = 'stage'
phoneNo = 8003030099
textMessage = "Hello There"
# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)



# import requests
# import json

# URL = 'https://www.way2sms.com/api/v1/createSenderId'

# # post request
# def sendPostRequest(reqUrl, apiKey, secretKey, useType, senderId):
#   req_params = {
#   'apikey':apiKey,
#   'secret':secretKey,
#   'usetype':useType,
#   'senderid':senderId
#   }
#   return requests.post(reqUrl, req_params)

# # get response
# response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'valid-sender-id')
# """
#   Note:-
#     you must provide apikey, secretkey, usetype and senderid values
#     and then requst to api
# """
# # print response if you want
# print response.text