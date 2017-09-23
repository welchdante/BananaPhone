from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC24c1d3865a9fdde26606a648cd4a166f"
auth_token = "783f98bc748f5490fd74879a421604d9"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+19896197341",
    from_="+19894484290",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)