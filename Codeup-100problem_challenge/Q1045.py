'''
automatic operation
1.summation
2.subtraction
3.multiplication
4.Quotient
5.remainder
6.Quotient + remainder
'''


x,y = input().split()
a = int(x)
b = int(y)
k = a/b
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print('%.2f'%(k))