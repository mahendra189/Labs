# calculate the angle
hour = int(input("Enter the time in hour: "))%12
minute = int(input("Enter the minutes: "))
angle_of_hour = 0.5*hour*60
angle_of_min = 6*minute
print(angle_of_hour)
print(angle_of_min)
angle_of_hour+=0.5*minute
print(angle_of_hour)
ang = abs(angle_of_hour-angle_of_min)
print(f"The angle between the hour and minute hand is: {ang}")