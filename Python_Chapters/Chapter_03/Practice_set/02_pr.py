letter = '''Dear <|NAME|>,
Greetings from ABC coding house, I am very happy to tell you about your selection

You are selected!
Have a great day Ahead!
Thanks and regards,
bill

Date: <|DATE|>
'''
name = input("Enter your name ")
date = input("Enter DATE ")
letter = letter.replace('<|NAME|>',name)
letter = letter.replace('<|DATE|>',date)
print(letter)