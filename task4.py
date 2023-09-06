# Write a Python program that matches a string that has an a followed by zero or one 'b'.

import re

pattern = '^ab?$'

print(re.match(pattern, 'abbbbb')) 
print(re.match(pattern, 'a')) # Match
print(re.match(pattern, 'ab')) # Match
print(re.match(pattern, 'abc'))