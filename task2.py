import re

pattern = '^ab*$'

print(re.match(pattern, 'abbbbb')) # Match
print(re.match(pattern, 'a')) # Match
print(re.match(pattern, 'ab')) # Match
print(re.match(pattern, 'abc'))