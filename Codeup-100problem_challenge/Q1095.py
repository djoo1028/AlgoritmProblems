'''
print the smallest number

'''

x = int(input())
y = input().split()

arr = []
for i in range(x):
    arr.append(int(y[i]))

arr.sort()
print(arr[0])