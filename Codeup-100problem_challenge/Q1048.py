'''

User input two integer and make output as a * 2^b

'''

def operation(arg1, arg2):
    a = arg1
    b = arg2
    print(a * 2 ** b)

x, y = input().split()
x = int(x)
y = int(y)

operation(x,y)