import cmath

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = cmath.sqrt(b**2 - 4*a*c)

root1 = (-b + discriminant) / (2*a)
root2 = (-b - discriminant) / (2*a)

print("Root 1:", root1)
print("Root 2:", root2)
