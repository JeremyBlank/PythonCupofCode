# Create an array of 5 integers and display array items, access them via index

from array import *
array_num = array('i', [1,3,5,7,9]) # Any numbers work
for i in array_num:
    print(i)
print('Access first three items individuals')
print(array_num[0])
print(array_num[1])
print(array_num[2])

# Append a new item to end of array
print('Starting array ', array_num)
array_num.append(11) # Adds number 11
print('new array: ', array_num)

# reverse the order
print(array_num[::-1])

# insert a new value before the number 3
print(array_num)
array_num.insert(1,4) # I want the number 4 at index of 2
print(array_num)

# Remove an item via index
array_num.pop(3) # default is last item, otherwise add index #(3) is index location
print(array_num)

# Remove the first occurrence of an element
new_array = array('i', [1,3,5,7,3,9,3,11])
print('new array: ', new_array)
new_array.remove(3) # Integer not index
print(new_array)

# convert an array into a list
print(type(new_array))
x = new_array.tolist()
print(type(x))
