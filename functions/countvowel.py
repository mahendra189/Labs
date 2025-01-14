def countvowels(s):
    count = 0
    for char in s:
        if char in ["a",'e','i','o','u']:
            count+=1
    return count

s = input("Enter a string: ")
print(f"Vowels in {s} is {countvowels(s)}")