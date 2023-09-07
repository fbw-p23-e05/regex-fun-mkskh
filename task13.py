import re

# Write a Python program that matches a word containing 'z', not the start or end of the word.


pattern = '(([A-Y][a-z]*)|[A-Y]|[a-y]+)z[a-y]+'

print(re.search(pattern, 'The quick brown fox jumps over the lazy dog.'))  # Match
print(re.search(pattern, 'Something')) 
print(re.search(pattern, 'Bla Bla Blaz.')) 
print(re.search(pattern, 'sa aksjfS Fassao Bzu salkl')) # Match
print(re.search(pattern, 'ABC Uuzu 123')) # Match
print(re.search(pattern, 'ABC Uuuuuzuuuuuuuuu 123')) # Match
