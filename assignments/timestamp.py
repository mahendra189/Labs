def takeTimestamp():
    print("Enter the timestamps: ")
    hour = int(input("hour: "))
    mint = int(input("minutes: "))
    sec = int(input("seconds: "))
    return hour,mint,sec

def printTime(time):
    return f"{time[0]}:{time[1]}:{time[2]}"
t1 = takeTimestamp()
printTime(t1)
t2 = takeTimestamp()
printTime(t2)

hour_diff = t2[0]-t1[0]
min_diff = t2[1]-t1[1]
sec_diff = t2[2]-t1[2]

print(hour_diff,min_diff,sec_diff)


# calculate the total time difference
# hour * 60 * 60
# min * 60
# sec
# add all to get the diff in sec
total =( hour_diff*60*60)+(min_diff*60)+sec_diff
print(f"Total timestamp diff between {printTime(t1)} and {printTime(t2)} is {total} seconds")