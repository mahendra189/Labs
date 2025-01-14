# # Assigments
# - program to find area of circle
r = int(input("Enter radius of the circle: "))
area = 3.14*r*r
print(f"The area of the circle is : {area}")






# - program to convert metre to kilometre
metre = int(input("Enter value in metres:"))
kilometers = metre/1000
print(f"{metre} m in kilometers is {kilometers}")
print("")
kilometers = int(input("Enter value in kilometers:"))
metres = kilometers*1000
print(f"{kilometers} km in metres is {metres}")






# - program to positive negative integer
a = int(input("Enter value of a: ") or '0')
if a:
    if a > 0:
        print(f"{a} is positive")
    elif a < 0:
        print(f"{a} is negative")
    else:
        print(f"{a} is equal to zero")
else:
    print("Enter a valid input")






# - program to find max of two numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("")
if a > b:
    print(f"Max is a: {a}")
    print(f"Min is b: {b}")
elif a<b:
    print(f"Max is b: {b}")
    print(f"Min is a: {a}")
else:
    print("a is equal to b")







# - program to find area of right angle triangle

b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
area = b*h/2
print(f"Area of right angled triangle is :{area}")








# - program to swap to numbers

a = 4
b = 3
print(f"Before {a} {b}")
temp = a
a = b
b = temp
print(f"After {a} {b}")

# easy one
def swap(a,b):
    return b,a
print(f"Before {a} {b}")
a,b = swap(a,b)
print(f"After {a} {b}")







# - program to display first n numbers 
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(i,end=" ")
print("Above is the list of n numbers")







# - program to calculate the factorial of the number

n = int(input("Enter a value to get factorial of that number: "))
s = n
i = n-1
while i>0:
    n *= i
    i-=1
print(f"Factorial of {s} is {n}")








# - display the number in the reverse order

n = int(input("Enter a value of n: "))
arr = list(range(1,n+1))
print(arr)
print(list(reversed(arr)))
    

arr = []
for i in range(1,n+1):
    arr.append(i)
print(reversed(arr))
print(list(reversed(arr)))








# - program to calculate sum and average of first n numbers 

import math
n = int(input("Enter value for n: " ))
arr = []
for i in range(1,n+1):
    arr.append(i)
print("Sum of arr: ",math.fsum(arr))
print("Average of arr: ",math.fsum(arr)/n)









# - find the sum of digits of a number
import math
n = int(input("Enter the value for n: "))
arr = [i for i in range(1,n+1)]

print(f"Sum till {n} is: ",math.fsum(arr))








# - display the first n multiples of a number
number = int(input("Enter the number: "))
n = int(input("Enter the number of n: "))
for i in range(1,n+1):
    print(f"{n} X {i} = {number*i}")








# - Display the first n numbers 
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(i,end=" ")
print("Above is the list of n numbers")








# - Program to calculate factorial of the number
n = int(input("Enter a value to get factorial of that number: "))
s = n
i = n-1
while i>0:
    n *= i
    i-=1
print(f"Factorial of {s} is {n}")








# - program to display the numbers in reverse order 

arr = []
for i in range(1,n+1):
    arr.append(i)
print(reversed(arr))
print(list(reversed(arr)))








# - Program to check if a number is prime

n = int(input("Enter n to check prime: "))
for i in range(2,n):
    if n%i == 0:
        print("Number is not prime number❌ ")
        exit()
print("Number is a prime Number✅")








# - Program to display first  n fibonacci numbers 

n = int(input("Enter value of n to get fibonacci Series till that >3: "))
if n <=3:
    print("n should greater than 3 !")
    exit()
print("0 1 1",end=" ")
last = 1
current = 1
# 1 2 3 4 5
# 0 1 1 2 3 5 8 13
for i in range(3,n):
    print(last+current,end=" ")
    temp = current
    current = current+last
    last = temp








# - Write all string functions
# try al the string functions

s = input("Enter a string: ")
print(s)
print("Length:\t",len(s))
print("Min: \t",min(s))
print("Max: \t",max(s))
print("Alphanumeric: \t",s.isalnum())
print("isAlpha: \t",s.isalpha())
print("isDigit: \t",s.isdigit())
print("isLower: \t",s.islower())
print("isUpper: \t",s.isupper())
print("Lowercase: \t",s.lower())
print("isupper: \t",s.upper())
print("isspace: \t",s.isspace())
print("isidentifier: \t",s.isidentifier())
print("endswith: \t",s.endswith("s"))
print("endswith: \t",s.endswith("s"))
print("startswith: \t",s.startswith('s'))
print("find: \t",s.find("s"))
print("count: \t",s.count("s"))
print("capitalize\t",s.capitalize())
print("title: \t",s.title())
print("swapcase: \t",s.swapcase())
print("replace: \t",s.replace('s','a'))
print("center: \t",s.center(10))
print("ljust: \t",s.ljust(5))
print("rjust: \t",s.rjust(5))
print("strip: \t",s.strip())
print("rstrip: \t",s.rstrip())
print("lstrip: \t",s.lstrip())











# - print all 3 index values in a string
string = input("Enter string: ")
s = []
i=0
while i <len(string):
    if i%3!=0:
        s.append(string[i])
    i+=1
print(''.join(s))







# - print if year is leaf year
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leaf year")
else:
    print(f"{year} is not a leaf year")








# - print maximum of 3 numbers

a,b,c = 1,2,3
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
else:
    print("c is maximum")








# - find roots of a quadratic equation
a = float(input("Enter coefficient of x^2: "))
b = float(input("Enter coefficient of x: "))
c = float(input("Enter value of c: "))
equ = f"{a}x^2 + {b}x + {c} = 0"
x1 = (-b+(b*b-(4*a*c))**(1/2))/2*a
x2 = (-b-(b*b-(4*a*c))**(1/2))/2*a

print(f"The roots of the equation {equ} are {x1} and {x2}")