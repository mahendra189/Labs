# calculate the angle
hour = int(input("Enter the time in hour: "))%12
minute = int(input("Enter the minutes: "))


def phase_1(hour,minute):
    angle_of_hour = 0.5*hour*60
    angle_of_min = 6*minute
    angle_of_hour-=0.5*minute
    ang = abs(angle_of_hour-angle_of_min)
    return ang

def phase_2(hour,minute):
    angle_of_hour = 0.5*hour*60
    angle_of_min = 6*(60-minute)
    angle_of_hour+=0.5*(minute)
    ang = 360-abs(angle_of_hour-angle_of_min)
    return ang

print(f"angle between {hour} hour {minute} min:",min(phase_1(hour,minute),phase_2(12-hour,minute)))