import re

# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.


pattern = '^[A-Za-z0-9\_]+$'

print(re.search(pattern, 'abcABC_123')) # Match
print(re.search(pattern, 'BlaA_a1Blaz')) # Match
print(re.search(pattern, 'py_tasks_14')) # Match
print(re.search(pattern, 'ABCUuuuuzuuuu_uuuuu123')) 
