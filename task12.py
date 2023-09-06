import re

# Write a Python program that matches a word containing 'z'.


pattern = '[A-Z]?[a-z]*z[a-z]*'

print(re.search(pattern, 'The quick brown fox jumps over the lazy dog.'))  # Match
print(re.search(pattern, 'Something')) 
print(re.search(pattern, 'Bla Bla Blaz.')) # Match
print(re.search(pattern, 'sa aksjfS Fassao Bz salkl')) # Match
print(re.search(pattern, 'ABC 123')) 
