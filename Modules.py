from math import *
import random as rnd
import statistics
print("Enter a number: ")
n = int(input())
print("log10(",n,"): ", log10(n))
print("\nRandom Number till range(",n,"): ", rnd.randrange(30))
a = int(input("\nEnter 1st Number: "))
b = int(input("\nEnter 2nd Number: "))
c = statistics.mean(a,b)
d = statistics.median(a,b)
print("Mean: ", c,"\nMedian: ", d)