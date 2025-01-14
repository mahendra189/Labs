dictionary = {
    'cars':10,
    'buses':5,
    'trucks':4
}
largest = 0
smallest = 1000
for value in dictionary.values():
    if value > largest:
        largest = value
    if value < smallest:
        smallest= value
    
print(f"maximum is {largest} and minimum is {smallest}")