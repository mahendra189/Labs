n = int(input("Enter value of n: "))

import math
print("Using math library")
print(math.factorial(n))

def factorial(n):
    if n<1:
        return 1 
    return n * factorial(n-1)
print("From Scratch")
print(factorial(n))
