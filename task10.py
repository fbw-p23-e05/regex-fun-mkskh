# Write a Python program that matches a word at the beginning of a string.

import re

pattern = '^[A-Z][a-z]+'

print(re.match(pattern, 'Alex Sar'))  # Match
print(re.match(pattern, 'Or Or')) # Match
print(re.match(pattern, 'a_/@67b sfdsf')) 
print(re.match(pattern, 'ABC DE')) 
