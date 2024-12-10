import math
n = int(input("Enter the value for n: "))
arr = [i for i in range(1,n+1)]

print(f"Sum till {n} is: ",math.fsum(arr))