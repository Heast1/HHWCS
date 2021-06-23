i = 1                               # initialize the iterator
num = 65                            # initialize the ASCII character to use
while i <= 6:
    j = 1                           # no. of letters to be printed per line
    while j<=i:
        print(chr(num), end=" ")    # print the alphabet
        j += 1
        num += 1
    print()                         # next line
    i += 1