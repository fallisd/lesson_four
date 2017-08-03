import re

sentence = "Hello. My name is David. I am 26 years old."


match = re.match('.*David.\\sI', sentence)
match2 = re.match(r'.*David.\\sI', sentence)
match3 = re.match(r'.*David.\sI', sentence)
match4 = re.match('.*David.\sI', sentence)


if(match):
    print("match1")
    print(match.group(0))
if(match2):
    print("match2")
    print(match2.group(0))
if(match3):
    print("match3")
    print(match3.group(0))
if(match4):
    print("match4")
    print(match4.group(0))