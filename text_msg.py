from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
#ACCOUNT_SID = "AC9e14bcdeae7fc1bc6c4dcba5ae41ad0d" 
#AUTH_TOKEN = "b77b297f9e355c3bb18a0d6ec2ffb27a" 

#test account
ACCOUNT_SID = "AC7db21ddc02ee81d13733399dbd222cfa" 
AUTH_TOKEN = "d15df7cbdf61673b807d64881791868a" 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
message=client.sms.messages.create(
    body="My name is me",
    to="+48665506351",
	from_="+48128810944",   
)

print message.sid
