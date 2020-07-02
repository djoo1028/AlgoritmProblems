'''
bitoperation

'''

'''
x = int(input())

a = ~x
b = int(a)
print(b)
'''


'''
Q1060
bitoperation 'AND'
'''
def bitOperation(arg1, arg2):
    a = int(arg1)
    b = int(arg2)
    print(a & b)
'''
Q1061
bitoperation 'OR'
'''

def bitOperation1(arg1, arg2):
    a = int(arg1)
    b = int(arg2)
    print(a | b)

'''
Q1062
bitoperation 'XOR'
'''

def bitOperation2(arg1, arg2):
    a = int(arg1)
    b = int(arg2)
    print(a ^ b)

x, y = input().split()
#bitOperation(x, y)
#bitOperation1(x, y)
bitOperation2(x, y)