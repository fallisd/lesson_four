import re

sentence = "Hello. My name is David. I am 26 years old."

# re.match(pattern, string)
# If zero or more characters at the beginning of string match the regular expression pattern, 
# return a corresponding MatchObject instance. 
# Return None if the string does not match the pattern; 
# note that this is different from a zero-length match.
match = re.match('David', sentence)

if (match):
    print('It was a match')
else:
    print('It was not a match')

match2 = re.match('.*David', sentence)

if (match2):
    print('It was a match')
else:
    print('It was not a match')

