# Write a Python program to remove leading zeros from an IP address.

import re

ip = '0001000.55.0010.080'
pattern = '0*(\d*)'
result = re.sub(pattern, r'\1', ip)

print(result)