# n = int(input("enter value of n: "))
# multiples = []
# for i in range(1,n):
#     if n%i==0:
#         multiples.append(i)
# print(f"Multiples of first n numbers is: {multiples}")


number = int(input("Enter the number: "))
n = int(input("Enter the number of n: "))
for i in range(1,n+1):
    print(f"{n} X {i} = {number*i}")
