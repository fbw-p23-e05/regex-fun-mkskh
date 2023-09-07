# Write a Python program that matches a word at the end of a string, with optional punctuation.

import re

pattern = '[A-Z]?[a-z]+\.?$'

print(re.search(pattern, 'Alex Sar'))  # Match
print(re.search(pattern, 'Or Or')) # Match
print(re.search(pattern, 'a_/@67b alex.')) # Match
print(re.search(pattern, 'a_/@67b max')) # Match
print(re.search(pattern, 'ABC 123')) 
