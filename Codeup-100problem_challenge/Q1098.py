'''
2d array
print location where is marked in matrix form
'''


#create the form of matrix
r,c = input().split()
arr = [[0 for col in range(int(c))] for row in range(int(r))]
#how many times iterate
a = int(input());
for i in range(a):
    l,d,x,y = input().split()
    if(d == '0'):
        for i in range(int(l)):
            arr[int(x) - 1][int(y)-1+i] = '1'
    else:
        for j in range(int(l)):
            arr[int(x) - 1 + j][int(y) - 1] = '1'

for i in range(int(r)):
    for j in range(int(c)):
        print(arr[i][j], end = ' ')
    print('')
