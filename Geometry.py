import math                                             # For math.pi

def area_square(side):                                  # defines the function for the area of square
    return side * side
def area_rectangle(length, breadth):                    # defines the function for the area of rectangle
    return length * breadth
def area_circle(radius):                                # defines the function for the area of circle
    return math.pi * radius * radius
def circumference_circle(radius):                       # defines the function for the circumference of circle
    return 2 * math.pi * radius

pre = "{:25} {:7}"

print(pre.format("Function", "Function name"))
print(pre.format("Area of Square", "Sqr"))
print(pre.format("Area of Rectangle", "Rect"))
print(pre.format("Area of Circle", "Circ1"))
print(pre.format("Circumference of Circle", "Circ2"))

print("\n")

print("Enter the operation you wanna perform: ")
operation = input()
operation.lower()

if operation == 'sqr':
    print("Enter the length of the side of square: ")
    a = float(input())
    opt = area_square(a)

elif operation == 'rect':
    print("Enter the length: ")
    a = float(input())
    print("Enter the breadth: ")
    b = float(input())
    opt = area_rectangle(a,b)

elif operation == 'circ1' or operation == 'circ2':
    print("Enter the radius: ")
    r = float(input())
    if operation == 'circ1': opt = area_circle(r)
    else: opt = circumference_circle(r)

else:
    opt = "Invalid operation"
print("The result of your operation is: ",opt)
