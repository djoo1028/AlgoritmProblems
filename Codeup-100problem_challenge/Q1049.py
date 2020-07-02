'''
Q1049
compare two different integer
if a is greater than b then print 1
if a is less than b then print 0

'''

def compare(arg1, arg2):
    a = arg1
    b = arg2
    if a > b:
        print('1')
    else:
        print('0')
'''
Q1050
If two input values are same print 1
Otherwise print 0

'''
def compare1(arg1, arg2):
    a = arg1
    b = arg2
    if a == b:
        print('1')
    else:
        print(0)

'''
Q1051
if b is greater than equal to a then print 1
Otherwise print 0
'''
def compare2(arg1, arg2):
    a = arg1
    b = arg2
    if b >= a:
        print('1')
    else:
        print('0')
'''
Q1052
if a and b are different print 1
otherwise print 0
'''

def compare3(arg1, arg2):
    a = arg1
    b = arg2
    if a != b:
        print('1')
    else:
        print('0')

x, y = input().split()
x = int(x)
y = int(y)

#compare(x,y)
#compare1(x,y)
#compare2(x,y)
compare3(x, y)