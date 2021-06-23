numbers = input("Enter the values to be processed(seperate each integer with space): ")
numbers = numbers.split(' ') # Splits the input into list

new_number = set(numbers)    # Sets list new_number as numbers
new_number.remove(max(new_number))  # Removes the max value from the list

print("The second largest number is ", max(new_number)) # Prints the 2nd largest number