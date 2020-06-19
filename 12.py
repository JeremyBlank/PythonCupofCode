# Accept a string and calculate number of letters and digits

s = input('Give me a string')
l, d = 0, 0
for c in s:
    if c.isalpha():
        l = l + 1
    elif c.isalpha():
        d = d + 1
    else:
        pass
print('Letters', 1)
print('Digits', d)

# Check the validity of a password
# At least 1 upper and lower [a-z]
# At least 1 number [0-9]
# At least 1 special character [!@#$%^&*]
# Minimum of 6 characters, max 16

import re
# re = regular expressions matching operations

p = input('Enter password: ')
x = True

while x:
    if (len(p) <6 or len(p)>16):
        break
    elif not re.search('[a-z]', p):
        break
    elif not re.search('[A-Z]', p):
        break
    elif not re.search('[0-9]', p):
        break
    elif not re.search('[!@#$%^&*]', p):
        break
    elif re.search('\s', p): # '\s' matches whitespace, so if any whitespace. Whitespace becomes true
        break
    else:
        print('Password check is good')
        x = False
        break
if x:
    print("Password check failed")

even_digits = []
for i in range(100,401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])==0):
        even_digits.append(s)
print(' $ '.join(even_digits))

# Create a program that will print out a pattern of an 'A'

letter_A = ''
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row !=0) or ((row ==0 or row ==3) and (column > 1 and column < 5))):
            letter_A = letter_A + '*'
        else:
            letter_A = letter_A + ' '
    letter_A = letter_A + '\n'
print(letter_A)