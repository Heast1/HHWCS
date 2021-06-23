print("Enter the string you wanna check(be sure to enter in lowercase!): ")
str = input()                               # Stores the user input in a memory location
str = str.lower()                           # Transforms the string to lowercase
reverse_str = str[::-1]                     # Reverses the string and stores to another memory location
print("Reversed String: ", reverse_str)
if(str == reverse_str):                     # Logical operation
    print(True, "It's a Palindrome.")
else:
    print(False, "It's not a Palidrome")
