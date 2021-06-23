x = 0                                   # Initializing the variables
y = 1
z = 1

print("Enter the limit: ")              # Gets user input
i = int(input())
print("{:10}".format(x,y),end ='  ')    # Prints the initial digits
while(z<=i):                            # Iterates through the loop
    print("{:10}".format(z), end='  ')
    x = y
    y = z
    z = x+y