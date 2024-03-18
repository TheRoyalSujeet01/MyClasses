import math
# Find Quadratic Equations
a = float(input("Enter Coefficient of a: "))
b = float(input("Enter coefficient of b: "))
c = float(input("Enter coefficient of c: "))
# Find the discriminant 
d = (b*b)-(4*a*c)
if d>0:
    e = float(math.sqrt(d))
    x1 = (-b+e)/(2*a)
    x2 = (-b-e)/(2*a)
    print("The roots are: {}, {}".format(x1, x2))
elif d==0:
    f = float(math.sqrt(d))
    x3 = (-b)/(2*a)
    print("The root is: ",x3)
else:
    print("Root is not defined")
