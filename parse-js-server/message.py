from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC0bec7092250cd3794b159a91b9dd1074" 
AUTH_TOKEN = "1569df3a5048cdcdbb2779b8b45924f1" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

sms = client.sms.messages.list() 
message = client.messages.get('SM97e5d64f12d6871f16e87a42c569adc6') 
 
print(sms)