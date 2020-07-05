'''

Random call between 1 and 23

first input integer n : how many times you are going to call numbers

second input : random call

output : how many times each number is called
'''

x = int(input())
y = input().split()
# Create Array
arr = []

# put 0 in array because to count
for i in range(24):
    arr.append(0)

for i in range(x):
    arr[int(y[i])] = arr[int(y[i])] + 1


for i in range(1, 24):
    print(arr[i], end = ' ')



'''
print the number in reverse

# '''
# def reverse(arg1, arg2):
#     pass
