def factorial(a):                         # Defines the factorial Function
    factorial = 1                         # Defines the initial term to 1
    i = 1                                 # Defines Increment for the loop
    if a == 0 or a < 0:                   # Returns the value to N/A or 0 since factorials of negative numbers doesn't exist
        if i == 0:
            return 0                      # Returns 0 as the answer
        else:
            return "Factorials of negative number doesn't exist"
    else:                                 # Calculates the factorial of a number
        while i <= a:
            factorial *= i                # Multiplies the factorial
            i += 1                        # Increments by 1
        return factorial                  # Returns the factorial

print("Enter the number you wanna find the factorial of: ")
a = int(input())                          # Gets the user input
n = factorial(a)                          # Calculates the value of the user input
print(str(a) + "! =",n)                   # prints the final value