import re

pattern = '^[A-Z][a-z]+$'

print(re.match(pattern, 'Maxim'))  # Match
print(re.match(pattern, 'maxim')) 
print(re.match(pattern, 'M')) 
print(re.match(pattern, 'MM')) 
print(re.match(pattern, 'm')) 
print(re.match(pattern, 'mm')) 
print(re.match(pattern, 'Pythonisgood')) # Match