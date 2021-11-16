from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from info import index
from database import connect,get_name,get_att,get_cgpa,get_fee
import re

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Everyone \n This is Charusat Student Assistance Whatapp Bot"

@app.route("/sms", methods=['POST'])
def sms_reply():

    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    i_d = ''
    msg = request.form.get('Body')
    msg = msg.lower()

    from_number = request.values.get('From')
    #to trim the phone number
    from_number = from_number[12:]

    resp = MessagingResponse()

    if msg == "hello":
        #resp = MessagingResponse()
        ans = index()
        resp.message(ans)
        return str(resp)

    elif re.search("^\d\d+[a-z][a-z]+\d\d\d$",msg):
        i_d = msg
        #resp = MessagingResponse()
        check = connect(i_d,from_number)
        resp.message(check)
        return str(resp)
    elif msg == 'show my name':
        ans=''
        if not i_d:
            ans = get_name('19It042',from_number)
        else:
            ans = get_name('19IT042',from_number)
        resp.message(ans)
        return str(resp)

    elif msg == 'show my cgpa':
        ans=''
        if not i_d:
            ans = get_cgpa('19It042',from_number)
        else:
            ans = get_cgpa('19IT042',from_number)
        resp.message(ans)
        return str(resp) 

    elif msg == 'show status of fee':
        ans=''
        if not i_d:
            ans = get_fee('19It042',from_number)
        else:
            ans = get_fee('19IT042',from_number)
        resp.message(ans)
        return str(resp) 

    elif msg == 'show my attendance':
        ans=''
        if not i_d:
            ans = get_att('19It042',from_number)
        else:
            ans = get_att('19IT042',from_number)
        resp.message(ans)
        return str(resp) 
        
    else:
        # Create reply
        #resp = MessagingResponse()
        resp.message("Sorry BOT is in development")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
