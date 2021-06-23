def InsertionSort(l):
    for i in l:
        j = l.index(i)
        while j>0:
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]
            else:
                break
            j -= 1
    return l
initial = input("Enter the list you wanna sort(seprated by space): ")
l = initial.split()
print("The unsorted list is: ", l)
print("The sorted list is: ", InsertionSort(l))