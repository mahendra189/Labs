# reverse using recursion

# def reverserecursion(n):
#     if n<=0:
#         return n
#     print(n%10,end="")
    # return reverserecursion(n//10)

# write recursion function to reverse a number is reverse of the given n 

def reverse(n):
    s = str(n)
    return s[::-1]

def reversereturnint(n,value=0):
    if n<=0:
        return value
    return reversereturnint(n//10,(value*10)+n%10)


def reversefunc(seq):
    for s in seq:
        print(reversereturnint(s))

s = [100,200,3300,400]
reversefunc(s)



