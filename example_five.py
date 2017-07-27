import re

sentence = "Hello. My name is David. I am 26 years old."

match = re.match('.*David.\\sI', sentence)
match2 = re.match(r'.*David.\\sI', sentence)

if(match):
    print("match1")
    print(match.group(0))
if(match2):
    print("match2")
    print(match2.group(0))