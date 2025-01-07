List = [1,2,3,4]
largest = List[0]
for i in range(1,len(List)):
    if List[i] > largest:
        largest = List[i]
print(f"Largest Element of the {List} is {largest} ")