import re

sentence = "Hello. My name is David. I am 26 years old."

# re.search(pattern, string)
# Scan through string looking for the first location where the regular expression pattern produces a match, 
# return a corresponding MatchObject instance. 
# Return None if the string does not match the pattern; 
# note that this is different from a zero-length match.
match = re.search('Dav([a-z][a-z])', sentence)

print(match.group(0))
print(match.group(1))