def RemoveVowels(str):
    vowels = "AaEeIiOoUu"                               # a string of vowels
    for i in str:
        if(i in vowels):
            str = str.replace(i, "")                    # replaces the char with space
    return str
print("Enter a line: ")
string = input()
print("The mutated string is ", RemoveVowels(string))