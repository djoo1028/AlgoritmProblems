'''
Return bigger number
Q1063
'''
def biggerNum(arg1, arg2):
    a = int(arg1)
    b = int(arg2)
    if a > b:
        print(a)
    else:
        print(b)

#x,y = input().split()
#biggerNum(x,y)

'''
Return the smallest number among three different int
Q1064
'''
def smallerNum(arg1, arg2, arg3):
    a = int(arg1)
    b = int(arg2)
    c = int(arg3)
    if a > b:
        if b > c:
            print(c)
        else:
            print(b)
    elif a < b:
        if a < c:
            print(a)
        else:
            print(c)
    else:
        print(a)

'''
Return even number

'''
def evenNum(arg1, arg2, arg3):
    a = int(arg1)
    b = int(arg2)
    c = int(arg3)
    even = [a,b,c]
    for i in range(len(even)):
        if even[i] % 2 == 0:
            print(even[i])
        else:
            pass

'''
Q1066
print as even if number is even
print as odd if number is odd
'''
def evenOdd(arg1, arg2, arg3):
    a = int(arg1)
    b = int(arg2)
    c = int(arg3)
    x_list = [a,b,c]
    for i in range(len(x_list)):

        if x_list[i] % 2 == 0:
            print('even')
        else:
            print('odd')

x,y,z = input().split()
#smallerNum(x,y,z)
#evenNum(x,y,z)
evenOdd(x,y,z)