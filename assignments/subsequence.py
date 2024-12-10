arr = [1,1,2,2,2,3,3,3,3,0]
max_count = 0
max_num = None
count = 0
current = arr[0]
for i in range(len(arr)):
    if current == arr[i]:
        count+=1
    else:
        if count >max_count:
            max_count = count
            max_num = current
            current = arr[i]
            count = 1
        else:
            count = 1
            current = arr[i]
    print(f"at {i} the count -> {count} of {current}")

maxi  = [max_num for _ in range(max_count)]
print(maxi)