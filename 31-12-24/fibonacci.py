n = int(input("Enter value of n to get fibonacci Series till that >3: "))
if n <=3:
    print("n should greater than 3 !")
    exit()
print("0 1 1",end=" ")
last = 1
current = 1
# 1 2 3 4 5
# 0 1 1 2 3 5 8 13
for i in range(3,n):
    print(last+current,end=" ")
    temp = current
    current = current+last
    last = temp

