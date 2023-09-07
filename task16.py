# Write a Python program to remove leading zeros from an IP address.

import re

ip = '000241.120.240.144'
pattern = '^0+'
result = re.sub(pattern, '', ip)

print(result)