# Write a Python program that starts each string with a specific number.


import re

for i in range(1,6):
    pattern = '^[0-9]+'
    inp = input('Write numbers that you want to see with specific number at the start (quantity unlimited): ')
    if re.match(pattern, inp):
        print(str(i)+'-'+inp)
        print('')
    else:
        print('Wrong format.')
        print('')
        pass

# I'm not sure that I understood the task correctly. Maybe this code is not what you wanted to see. Please write some feedback about this task    