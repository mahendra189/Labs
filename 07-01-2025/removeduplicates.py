List = [1,1,1,2,2,3,3]
final = []
duplicate = []
for n in List:
    if n not in duplicate:
        duplicate.append(n)
        final.append(n)
print("No Duplicate List: " ,final)