def toggleCase(str):                        # define toggle case function
    ret = ""                                # initialize the string to be returned
    i = True                                # Capitalize
    for char in str:
        if i:
            ret += char.upper()             # change the character case and add it to the string
        else:
            ret += char.lower()
        if char != ' ':
            i = not i                       # changes the boolean value of i
    return ret                              # returns the statement

print("Enter the string you wanna toggle: ")
str = input()                               # gets the input from the user
print(toggleCase(str))