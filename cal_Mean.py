def cal_Mean(num):
    n = len(num)
    sum = 0
    for i in range(0, n):
        sum += int(num[i])
    mean = sum/n
    return mean
print("Enter the list of numbers: ")
j = input()
j = j.split()
print("The mean of the list", j, "is ", cal_Mean(j))