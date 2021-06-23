def Max(num1, num2, num3):                                  # Function to find the maximum input
    if  num1 < num2 and num2 > num3:                        # Python has officially triggered the entire software industry
        return num2                                         # returns num2 as the max
    if  num1 > num2 and num1 > num3:
        return num1
    if num1 < num3 and num1 < num3:
        return num3
    return "All the values are equal"

print("Enter the 3 numbers (seperated by space): ")

a = input()                                                 # Gets input from the user
a = a.split(' ')                                            # Splits the input into an array

b = Max(a[0], a[1], a[2])                                   # Calls the function Max
print("The maximum number in the input is: ",b)             # Prints the result