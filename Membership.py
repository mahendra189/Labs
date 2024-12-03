# check the membership operator in python for python labs

a = [1,2,3,4]
b = a
print(b is a)


#  print the memory locatino of the array in python 
print(id(a))


# get all the methods of the current function of the value

for value in a.__dir__():
    print(value)

