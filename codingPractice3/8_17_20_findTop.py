'''


'''
import sys
sys.stdin = open('input.txt')
# 상하좌우 비교할떄
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

a = int(input())
num = [list(map(int, input().split())) for _ in range(a)]

num.insert(0, [0] * a)
num.append([0] * a)

for x in num:
    x.insert(0,0)
    x.append(0)

cnt = 0
for i in range(1, a+1):
    for j in range(1, a+1):
        if all(num[i][j] > num[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)