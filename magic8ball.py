import random
print('ask your question')
input()
messages = ['it is certain',
            'it is decidedly so',
            'yes',
            'reply hazy, try again',
            'ask again later',
            'concentrate and ask again',
            'my reply is no',
            'it does not look good',
            'very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
