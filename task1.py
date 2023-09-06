import re

#I wrote 2 options. The first option checks for the presence of at least 1 type of characters (for example, the string will only contain small letters "abc"). The second option checks that all types of characters must be required (for example, the string will contain small letters, large letters and numbers "ABCabc123")

#FIRST

text = "abc"

pattern = '^[A-Za-z0-9]+$'

print('\n First option \n')

if re.match(pattern, text):
    print('The string contains at least 1 type of characters from the set of characters (a-z, A-Z and 0-9)')
else:
    print("String does not match pattern")

# SECOND

text = "ABCabc123"

pattern = '^([A-Z]+[a-z]+[0-9]+)+$'

print('\n Second option \n')

if re.match(pattern, text):
    print('The string contains all types of characters from the set of characters (a-z, A-Z and 0-9)')
else:
    print("String does not match pattern")