'''
첫째 줄에 사람의 수 N이 주어진다. N은 10보다 작거나 같은 자연수이다.

둘째 줄에는 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지 주어진다.

i번째 수는 0보다 크거나 같고, N-i보다 작거나 같다.

input
4
2 1 1 0

output
4 2 1 3
'''
import time

# Type how many input values will take
x = int(input())
# Put typed number into the list
arr = list(map(int, input().split()))
# Check time
start = time.time()
# Empty list
list = []

# Check element from end because the largest number will have less possibility than
# smaller number
for i in range(len(arr)-1, -1 , -1):
    # list.insert(a,b) -> put value of b into the list at a spot
    list.insert(arr[i], i + 1)

for i in list:
    print(i, end = ' ')
print('')
print('Time :', time.time() - start)