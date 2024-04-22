import math

# Read input from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Check whether the values fit the sides of a triangle
if a + b > c and a + c > b and b + c > a:
    # Calculating angle values using the law of geometry for angles in
    angle_A = round(math.degrees(math.acos((b**2 + c**2 - a**2) /
 (2 * b * c))), 2)
    angle_B = round(math.degrees(math.acos((a**2 + c**2 - b**2) /
 (2 * a * c))), 2)
    angle_C = round(180 - angle_A - angle_B, 2)

    print("Angles of the triangle are:")
    print("Angle A:", angle_A)
    print("Angle B:", angle_B)
    print("Angle C:", angle_C)
else:
    print("False")
