import random
print('ask your question')
input()
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'it is decidedly so'
    elif answerNumber == 3:
        return 'yes'
    elif answerNumber == 4:
        return 'reply hazy, try again'
    elif answerNumber == 5:
        return 'ask again later'
    elif answerNumber == 6:
        return 'concentrate and ask again'
    elif answerNumber == 7:
        return 'my reply is no'
    elif answerNumber == 8:
        return 'it does not look good'
    elif answerNumber == 9:
        return 'very doubtful'
r = random.randint(1,9)
fortune = getAnswer(r)
print (fortune)
