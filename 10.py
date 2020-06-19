# Reverse an input str

x = input('Type what you want to reverse: ')
b = ''.join(reversed(x))  # '' is a str
print(b)

# or, use a start and step. Slices str setps 0f -1
print(x[::-1])


# Count even or odd from a series of numbers

def oddEventCount(x):
    odd_count = 0
    even_count = 0
    for i in x:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return "odd cound: " + str(odd_count) + "\teven count: " + str(even_count)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(oddEventCount(x))

# Given the below list, print out the item and its type

data = [1452, 11.23, 1 + 2j, True, 'w3resourse', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

for icecream in data:
    print('Type of ', icecream, ' is ', type(icecream))

# Write program prints all numbers except 3 and 6

for i in range(7):
    if i != 3 and i != 6:
        print(i)
print('\n')

# Program a fibonacci seq between 0 and 50. Next number is found by adding 2 numbers before it
x,y = 0,1
while y < 50:
    print(y)
    x,y = y, x+y

print('\n')

# Write a program iterating 0 to 50. If num is multiple of 3 print SUPAAA instead of num.
# if num is multiple of 5 print  BADASS. If num is multiple of both print super badass

for moomoo in range(1,50):
    if moomoo % 3 ==0:
        print('SUPPA')
    elif moomoo % 5 ==0:
        print('BADASS')
    elif moomoo % 3==0 and moomoo % 5==0:
        print('superbadass')
    else:
        print(moomoo)