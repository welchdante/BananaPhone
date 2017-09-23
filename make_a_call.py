from twilio.rest import Client
import config

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+19896197341",
    from_="+19894484290",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)