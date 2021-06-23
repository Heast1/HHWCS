n = int(input("Enter the limit of the countries you wanna add: "))
i = 1
country = dict()
while i <= n:
    count     =   input("Country name: ")
    capital     =   input("Capital Name: ")
    currency    =   input("Currency: ")
    country[count] = (capital, currency)
    i += 1
l = country.keys()
print("\nCountry\t\t","Capital\t\t","Currency")
for i in l:
    z = country[i]
    print('\n', i, '\t\t', end="")
    for j in z:
        print(j, '\t\t', end="\t\t")
x = input("\nEnter country to be searched: ")
for i in l:
    if i==x:
        print("\nCountry\t\t","Capital\t\t","Currency\t\t")
        z = country[i]
        print('\n',i,'\t\t',end="")
        for j in z:
            print(j,'\t\t',end="\t\t")
        break
