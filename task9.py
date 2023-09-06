import re

pattern = '^a.*b$'

print(re.match(pattern, 'asjsdhjhfjdshb'))  # Match
print(re.match(pattern, 'ab')) # Match
print(re.match(pattern, 'a_/@67b')) # Match
print(re.match(pattern, 'ABC')) 
