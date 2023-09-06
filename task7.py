import re

pattern = '^(_?[a-z]+_+[a-z]+(_+[a-z])?)+$'

print(re.match(pattern, 'adsf_bdf'))  # Match
print(re.match(pattern, 'a_b')) # Match
print(re.match(pattern, 'a_b_c_d')) # Match
print(re.match(pattern, 'a_b_c_d_eldsklfl')) # Match
print(re.match(pattern, 'a'))
print(re.match(pattern, 'abcde'))