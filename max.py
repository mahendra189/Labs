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
