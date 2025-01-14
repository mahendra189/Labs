def maxtwonum(a,b):
    if a>b:
        return a
    else:
        return b

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print(f"The mas of the two numbers is : {maxtwonum(a,b)}" )