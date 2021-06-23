phoneBook = dict()
n = int(input("Enter the total length of the dictionary: "))
i = 1
while (i <= n):
    a = input("Contact Name: ")
    b = input("Phone Number: ")
    phoneBook[a] = b
    i += 1
pre = '{:12} {:12}'
print(pre.format("Name", "Phone Number"))
for i in phoneBook:
    print(pre.format(i, phoneBook[i]))