def reverse():
    n = input("Enter a value for n: ")
    for i in range(len(n)-1,-1,-1):
        print(n[i],end="")
    print(" ")
reverse()

def reverse2():
    n = input("Enter a value for n: ")
    print(n[::-1])
reverse2()