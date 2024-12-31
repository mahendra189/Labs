import math
a = int(input("Enter No. of Students in A: "))
b = int(input("Enter No. of Students in B: "))
c = int(input("Enter No. of Students in C: "))

def assign(students):
    return math.ceil(students/2)

for i in [a,b,c]:
    print(f"{i} students will need {assign(i)} desks.")
