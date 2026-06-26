from cmath import sqrt

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b**2) - (4*a*c)
sol1 = (-b - sqrt(d)) / (2*a)
sol2 = (-b + sqrt(d)) / (2*a)

print("Solutions:\nX1 =", sol1, "\nX2 =", sol2)