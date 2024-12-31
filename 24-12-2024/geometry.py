# from collections import namedtuple

# Point = namedtuple("Point",['x','y'])
# p1 = Point(1,2)
# print(p1.x)

class Point():
    def _init_(self,point):
        self.point = point
        points = [int(a) for a in input(f"Enter coordinates for {point} x y: ").split()]
        self.x = points[0]
        self.y = points[1]
        
p1 = Point(1)
p2 = Point(2)
p3 = Point(3)

def check(p1,p2,p3):
    return p1.x == p2.x and (abs(p3.y) == abs(p1.y) or abs(p3.y) == abs(p2.y))



if check(p1,p2,p3):
    if p1.y == p3.y:
        x = p3.x
        y = p2.y
    else:
        x = p3.x
        y = p1.y
    print(f"The fourth coordinate of the rectangle is: ({x},{y})")
elif check(p1,p3,p2):
    if p1.y == p2.y:    
        x = p3.x
        y = p2.y
    else:
        x = p2.x
        y = p1.y

    print(f"The fourth coordinate of the rectangle is: ({x},{y})")
else:
    print("Invalid Coordinates of the rectangle!!")