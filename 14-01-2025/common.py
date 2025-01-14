set1 = {1,2,3}
set2 = {3,4,5}
print("Common elements are: ",set1.intersection(set2))

set1.difference(set1.intersection(set2))
print("Remove the interesection elements")