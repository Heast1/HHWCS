def LinearSearch(query, n ,x): # Linear Search: O(n)
    for i in range(0, n):
        if query[i] == x:
            return i
    return -1

print("Enter the list of number you wanna search through: ")
query = input().split()
print("Enter the query you wanna find: ")
x = input()
n = len(query)
result = LinearSearch(query, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)