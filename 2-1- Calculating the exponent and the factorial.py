#Read input from user
a = float(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Calculate the exponent 
if b >= 0:
    #First method
    result = 1
    for _ in range(b):
        result *= a
    print("The result of", a, "^", b, "is:", result)
    #second method
    # result = 1
    # power = b
    # while power > 0:
    #     result *= a
    #     power -= 1
    # print("The result of", a, "^", b, "is:", result)
    # Factorial calculation of the 
    
#===============================================================
    #First method
    factorial_result = 1
    for i in range(1, int(result) + 1):
        factorial_result *= i
    print("The factorial of", result, "is:", factorial_result)
    #second method
    # i = 1
    # while i <= result:
    #     factorial_result *= i
    #     i += 1
    # print("The factorial of", result, "is:", factorial_result)
else:
    print("b must be a non-negative integer")
