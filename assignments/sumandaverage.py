import math
n = int(input("Enter value for n: " ))
arr = []
# loop from 1 to n and append the values to a list
# get the sum of the elements using fsum function
for i in range(1,n+1):
    arr.append(i)
print("Sum of arr: ",math.fsum(arr))
print("Average of arr: ",math.fsum(arr)/n)