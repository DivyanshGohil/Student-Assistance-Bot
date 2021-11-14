from emoji import emojize
from emoji.core import emojize

def index():
    q1 = emojize(":right_arrow:")+" *Hello,This is Charusat Student Assistance Bot (created by-19IT041/19IT042)*\n"
    q2 = emojize(":right_arrow:")+ " Type *College id* to authenticate yourself"
    q = q1 + q2
    return q

def not_id():
    q1 = emojize(":loudly_crying_face:")+ "Your id is not matching with your mobile number\n"
    q2 = emojize(":right_arrow:") + "Check your Id"
    q = q1 + q2
    return q

def verify():
    q1 = emojize(":grinning_face:")+ 'Authentication Complete\n'
    q2 = emojize(":right_arrow:") + " *Try this questions*.\n1: Show my name\n2: Show my cgpa\n3: Show status of fee\n"
    q3 = "4: Show my attendance"
    return q1+q2+q3