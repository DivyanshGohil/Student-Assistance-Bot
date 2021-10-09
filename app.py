from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from info import index

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Everyone \n This is Charusat Student Assistance Whatapp Bot"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
