# find number positive or negative or zero
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