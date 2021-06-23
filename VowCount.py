def VowCount(str):          # Defines the VowCount 
    vow = list(str.split()) # Splits the string into list
    count = 0               # Initialize count
    vowel = "aeiouAEIOU"    # Vowels in english alphabets
    for i in vow:           # For loop to check whether the elements starts with vowels or not
        if i[0] in vowel:
            count += 1      # Increments the count by +1
    return count

print("Enter the string of line: ")
str = input()
print("Total Number of words starting with Vowels are: ", VowCount(str))