'''
Three input
1.add three values
2.calculate average and round up at the first decimal place
'''
import math


x,y,z = input().split()
a = int(x)
b = int(y)
c = int(z)
summation = a + b + c
average = (summation)/3
print(summation)
print(round(average,1))