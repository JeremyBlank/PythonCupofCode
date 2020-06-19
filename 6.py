# Create a calculator

c = 50
h = 30

# use this formula Q = square root lf [(2*c*d)/h]
# find d

import math

x = []
y = [i for i in input('Give me a number: ').split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))

# the join method is for str so we need to conver our integer answer to a str to use the join method
# PEMDAS...
# Please
# Excuse
# My
# Dear
# Aunt
# Sally