def BubbleSort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
initial = input("Enter the list you wanna sort(seprated by space): ")
l = initial.split()
print("The unsorted list is: ", l)
print("The sorted list is: ", BubbleSort(l))