import re

# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


pattern = '^[A-Za-z0-9\_]+$'

print(re.search(pattern, 'The quick brown fox jumps over the lazy dog.'))  # Match
print(re.search(pattern, 'abcABC123')) 
print(re.search(pattern, 'BlaAa1Blaz')) 
print(re.search(pattern, 'sa aksjfS Fassao Bzu salkl')) # Match
print(re.search(pattern, 'py_tasks_14')) # Match
print(re.search(pattern, 'ABC Uuuuuzuuuuuuuuu 123')) # Match
