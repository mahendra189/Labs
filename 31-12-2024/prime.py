n = int(input("Enter n to check prime: "))
for i in range(2,n):
    if n%i == 0:
        print("Number is not prime number❌ ")
        exit()
print("Number is a prime Number✅")



for i in range(2,n):
    if n%i ==0:
        break
else:
    print('Prime')
    exit()
print("Not Prime")