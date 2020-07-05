'''
print number in reverse

'''


x = int(input())
y = input().split()
arr = []
for i in range(x):
    arr.append(y[i])

arr.reverse()
for i in range(len(y)):
    print(arr[i], end = ' ')
