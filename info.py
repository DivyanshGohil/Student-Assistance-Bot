import emoji

def index():
    q1 = emoji.emojize(":right_arrow:")+" *Hello,This is Charusat Student Assistance Bot (created by-19IT041/19IT042)*\n"
    q2 = emoji.emojize(":right_arrow:")+ " Type *College id* to authenticate yourself"
    q = q1 + q2
    return q

def question():
    q = emoji.emojize(":right_arrow:")+ " *Step 1*: Enter your *userid* to authenticate yourself"
    return q


print(index())