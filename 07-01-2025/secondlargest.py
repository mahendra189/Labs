List = [1,2,3,4]
largest = List[0]
for i in range(1,len(List)):
    if List[i] > largest:
        largest = List[i]
List.remove(largest)
secondLargest = List[0]
for i in range(1,len(List)):
    if List[i] > secondLargest:
        secondLargest = List[i]
print(f"Second Largest element of the list is {secondLargest} and first largest is {largest}")