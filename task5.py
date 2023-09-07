# Write a Python program that matches a string that has an a followed by three 'b'.


import re

pattern = '^ab{3}$'

print(re.match(pattern, 'abbb'))  # Match
print(re.match(pattern, 'a')) 
print(re.match(pattern, 'ab')) 
print(re.match(pattern, 'abc'))