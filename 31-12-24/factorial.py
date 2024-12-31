n = int(input("Enter a value to get factorial of that number: "))
s = n
i = n-1
while i>0:
    n *= i
    i-=1
print(f"Factorial of {s} is {n}")