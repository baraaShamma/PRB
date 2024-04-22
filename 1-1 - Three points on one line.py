# Read input from user
x1 = float(input("Enter the x of point 1: "))
y1 = float(input("Enter the y of point 1: "))
x2 = float(input("Enter the x of point 2: "))
y2 = float(input("Enter the y of point 2: "))
x3 = float(input("Enter the x of point 3: "))
y3 = float(input("Enter the y of point 3: "))

# Calculate the slope between the points (x1, y1) and (x2, y2)
if x2 != x1:
    slope1 = (y2 - y1) / (x2 - x1)
else:
    slope1 = None
# Calculate the slope between the points (x2, y2) and (x3, y3)
if x3 != x2:
    slope2 = (y3 - y2) / (x3 - x2)
else:
    slope2 = None

# Check whether the points are on the same line
if slope1 == slope2:
    print("True")
else:
    print("False")
