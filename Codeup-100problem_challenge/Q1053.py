'''
if input value is 1 print 0
if input value is 0 then print 1

'''

def logical(arg1):
    a = arg1
    if a == 1:
        print('0')
    else:
        print('1')
'''
Q1054
if True and True then print 1
otherwise print 0
'''

def logical1(arg1, arg2):
    a = arg1
    b = arg2
    if ((a == 1) and (b == 1)):
        print('1')
    else:
        print('0')

'''
Q1055
Or statement

'''

def logical2(arg1, arg2):
    #result = '0'
    a = arg1
    b = arg2
    x_list = [a,b]
    result = any(x_list)
    if result == True:
        print('1')
    else:
        print('0')


'''
Q1056
print 1 if True != False
print 0 if True = True / False = False

'''

def logical3(arg1, arg2):
    a = arg1
    b = arg2
    if a != b:
        print('1')
    else:
        print('0')

'''
Q1057
Truth table

'''
def logical4(arg1, arg2):
    a = arg1
    b = arg2
    if a == b:
        print('1')
    else:
        print('0')
'''
Q1058
print 1 when a anb b both are false
otherwise print 0
'''
def logical5(arg1, arg2):
    a = arg1
    b = arg2
    if ((a == 0) and (b == 0)):
        print('1')
    else:
        print('0')

#x = int(input())
x , y = input().split()
x = int(x)
y = int(y)
#logical(x)
#logical1(x,y)
#logical2(x,y)
#logical3(x,y)
#logical4(x,y)
logical5(x,y)
