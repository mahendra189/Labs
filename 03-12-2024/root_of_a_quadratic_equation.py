# roots of the quadratic equation'

a = float(input("Enter coefficient of x^2: "))
b = float(input("Enter coefficient of x: "))
c = float(input("Enter value of c: "))
equ = f"{a}x^2 + {b}x + {c} = 0"
x1 = (-b+(b*b-(4*a*c))**(1/2))/2*a
x2 = (-b-(b*b-(4*a*c))**(1/2))/2*a

print(f"The roots of the equation {equ} are {x1} and {x2}")