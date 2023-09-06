import re

# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

text1 = "abc123ABC"
text2 = "abc12@3ABC"

pattern = '^[A-Za-z0-9]+$'

print('Checking text 1 - abc123ABC')

if re.match(pattern, text1):
    print(text1, 'contains the required set of characters ( a-z, A-Z and 0-9)')
else:
    print(text1, "does not match pattern")

print('')
print('Checking text 2 - abc12@3ABC')

if re.match(pattern, text2):
    print(text2, 'contains the required set of characters ( a-z, A-Z and 0-9)')
else:
    print(text2, "does not match pattern")

