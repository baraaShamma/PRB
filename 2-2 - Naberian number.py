#Read input from user
n = int(input("Enter the value of n: "))

e = 1  #The first value in the string
factorial = 1  # Current Napierian number (1!)
i = 1

while i <= n:
    factorial *= i  # Calculating the current factorial number
    e += 1 / factorial  # Add the new part to the value of the Napierian number
    i += 1

print("The value of e is:", e)

