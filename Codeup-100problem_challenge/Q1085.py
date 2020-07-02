'''

calculate sound storage size

'''
import math
def cal(arg1, arg2, arg3, arg4):
    h = int(arg1)
    b = int(arg2)
    c = int(arg3)
    s = int(arg4)

    bit = (h * b * c * s)/ 8
    megabyte = bit / (1024 ** 2)
    print(round(megabyte,1), 'MB')

'''
calculate image storage
'''
def calImage(arg1, arg2, arg3):
    w = int(arg1)
    h = int(arg2)
    b = int(arg3)

    bit = (w * h * b) / 8
    megabyte = bit/(1024 ** 2)
    print('{:.2f} {}'.format(megabyte, 'MB'))


def addSum(arg1):
    a = int(arg1)
    i = 0
    result = 0
    while result < a:
        i += 1
        result = i + result
    print(result)

def notThree(arg1):
    a = int(arg1)
    i = 0
    while i < a:
        i += 1
        if i % 3 == 0:
            pass
        else:print(i, end = ' ')


x = input()
notThree(x)
#addSum(x)
#x,y,z = input().split()
#calImage(x,y,z)
#x,y,z,w = input().split()
#cal(x,y,z,w)