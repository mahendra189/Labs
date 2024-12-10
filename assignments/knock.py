N = int(input("Enter the Number of Pins: "))
pins = ["|"]*N
K = int(input("Enter the Number of Balls: "))
start = [0]*K
end = [0]*K
for i in range(K):
    # provide values of start and stop for each ball
    start[i] = int(input(f"Enter the start of the range for ball {i}: "))
    end[i] = int(input(f"Enter the end of the range for ball {i}: "))
# start rolling
for i in range(K):
    for k in range(start[i],end[i]+1):
        pins[k-1] = "."
print("The remaining Pins are: ",pins)

