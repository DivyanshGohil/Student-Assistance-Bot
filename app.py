from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from info import index, question
from database import connect
import re

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Everyone \n This is Charusat Student Assistance Whatapp Bot"

@app.route("/sms", methods=['POST'])
def sms_reply():

    # FLAG FOR ID VERIFICATION
    flag = False
    """Respond to incoming calls with a simple text message."""
    # Fetch the message

    msg = request.form.get('Body')
    msg = msg.lower()

    from_number = request.values.get('From')
    #to trim the phone number
    from_number = from_number[12:]

    resp = MessagingResponse()

    if msg == "info":
        #resp = MessagingResponse()
        ans = index()
        resp.message(ans)
        return str(resp)

    elif msg == 'myno':
        #resp = MessagingResponse()
        ans = from_number
        resp.message(ans)
        return str(resp) 

    elif re.search("^\d\d+[a-z][a-z]+\d\d\d$",msg):
        #resp = MessagingResponse()
        check = connect()
        resp.message(check)
        return str(resp) 
        
    else:
        # Create reply
        #resp = MessagingResponse()
        resp.message("You said this: {}".format(msg))

        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
