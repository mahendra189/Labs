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