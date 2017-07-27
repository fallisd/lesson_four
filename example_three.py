import re

sentence = "Hello. My name is David. I am 26 years old."

# re.sub(pattern, repl, string)
# Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. 
# If the pattern isn’t found, string is returned unchanged.
new = re.sub('Dav[a-zA-Z][a-zA-Z]', 'Watson', sentence)

print(new)

