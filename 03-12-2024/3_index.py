string = input("Enter string: ")
s = []
i=0
while i <len(string):
    if i%3!=0:
        s.append(string[i])
    i+=1
print(''.join(s))