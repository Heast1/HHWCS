lst = list()
choice = 0
while True:
    pre = '{:7} {:7}'
    print("Menu")
    print(pre.format("1.", "Append an element"))
    print(pre.format("2.", "Insert an element"))
    print(pre.format("3.", "Append a list to the given list"))
    print(pre.format("4.", "Modify an existing element"))
    print(pre.format("5.", "Delete an existing element from its position"))
    print(pre.format("6.", "Delete an existing element with a given value"))
    print(pre.format("7.", "Sort the list in ascending order"))
    print(pre.format("8.", "Sort the list in descending order"))
    print(pre.format("9.", "Display the list"))
    choice = int(input("\nChoose your input: "))
    # append an element
    if choice == 1:
        element = int(input("\nEnter the element you wanna append: "))
        lst.append(element)
        print("\nThe element had been appended.")
    # Insert an element at desired position
    elif choice == 2:
        element = int(input("\nEnter the element to be appended: "))
        pos = int(input("\nEnter the position: "))
        lst.insert(pos, element)
        print("\nThe element had been inserted.")
    # Append a list to the original list
    elif choice == 3:
        newList = int(input("\nEnter the new list: "))
        lst.append(newList)
        print("\nThe list has been appended.")
    # Modify an exiting element
    elif choice == 4:
        i = int(input("\nEnter the position of the element to be modified: "))
        if i < len(lst):
            newElement = int(input("\nEnter the new element: "))
            oldElement = lst[i]
            print("\nThe element", oldElement,"has been modified.")
        else:
            print("\nPosition of the element exceeds the list length.")
    # Delete an existing element from its position
    elif choice == 5:
        i = int(input("\nEnter the position of the element to be deleted: "))
        if i < len(lst):
            element = lst.pop(i)
            print("\nThe element",element,"has been deleted.")
        else:
            print("\nPosition of the element exceeds the list length.")
    # delete an existing element by the value
    elif choice == 6:
        element = int(input("\nEnter the element to be deleted: "))
        if element in lst:
            lst.remove(element)
            print("\nThe element",element,"has been deleted.")
        else:
            print("\nPosition of the element exceeds the list length.")
    # List in sorted order
    elif choice == 7:
        lst.sort()
        print("\nThe list has been sorted.")
    # List in reverse sorted order
    elif choice == 8:
        lst.sort(reverse = True)
        print("\nThe list has been sorted in reverse order.")
    # Display the list
    elif choice == 9:
        print("\nThe list is: ", lst)
    