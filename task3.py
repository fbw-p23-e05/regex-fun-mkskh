# Write a Python program that matches a string that has an a followed by one or more b's.

import re

pattern = '^ab+$'

print(re.match(pattern, 'abbbbb')) # Match
print(re.match(pattern, 'a'))
print(re.match(pattern, 'ab')) # Match
print(re.match(pattern, 'abc'))