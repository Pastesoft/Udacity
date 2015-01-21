from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACf681c6c5f12645edac3e06a76b34b61e"
auth_token  = "4835e401e9ca571bbab05474e117fba0"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body="Hi Vita, this is from Steo: I <3 u",
        to="+447475798788",    # Replace with your phone number
        from_="+441736322062") # Replace with your Twilio number
print message.sid
