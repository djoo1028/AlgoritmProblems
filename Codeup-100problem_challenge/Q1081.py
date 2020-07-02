'''
Q1081
Create matrix within
typed range
for example, if user type 2 3
then
1 1
1 2
1 3
2 1
2 2
2 3

'''
def matrix(arg1, arg2):
    a = int(arg1)
    b = int(arg2)
    for i in range(a):
        for j in range(b):
            print('{:d} {:d}'.format(i+1,j+1))
'''
Q1082
multiplication table with hex
character -> integer : int(input, decimal) -> int(x, 16) : hexa
integer -> character : hex(x), ox(x)...
'''
def table(arg1):
    a = arg1
    for i in range(1,16):
        i = hex(i)
        hex_c = hex(a)
        hex_c_up = hex_c[2:].upper()
        i_index = i[2:]
        i_index_up = i_index.upper()
        result = int(i_index_up,16) * a
        result_hex = hex(result)
        result_hex_up = result_hex[2:].upper()
        #print(result)
        print('{0}*{1}={2}'.format(hex_c_up,i_index_up,result_hex_up))
'''
Q1083
3,6,9 game
we have to print X every number that is divided by 3
'''
def numberGame(arg1):
    a = int(arg1)
    for i in range(1,a+1):
        if i % 3 == 0:
            print('X', end=' ')
        else:print(i, end=' ')


'''
Q1084
print 3 * 3 matrix with user input
'''

def threeMatrix(arg1, arg2, arg3):
    a = int(arg1)
    b = int(arg2)
    c = int(arg3)

    t = 0
    for i in range(a):
        for j in range(b):
            for k in range(c):
                t += 1
                print(i,j,k)
    print(t)

x,y,z = input().split()
threeMatrix(x,y,z)

#numberGame(x)
#x = int(x, 16)
#table(x)
#x,y = input().split()
#matrix(x,y)
#print(type(x[0]))
#print(type(x[1]))
