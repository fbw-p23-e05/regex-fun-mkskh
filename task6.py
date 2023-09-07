# Write a Python program that matches a string that has an a followed by two to three 'b'.


import re

pattern = '^ab{2,3}$'

print(re.match(pattern, 'abbb'))  # Match
print(re.match(pattern, 'a')) 
print(re.match(pattern, 'abb')) # Match
print(re.match(pattern, 'abbbb'))