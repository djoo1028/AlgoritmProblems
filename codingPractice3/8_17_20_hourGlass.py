# '''
#
#
#
# '''
# import sys
# sys.stdin = open('input.txt')
# a = int(input())
# num = [list(map(int, input().split())) for _ in range(a)]
# b = int(input())
#
# for i in range(b):
#     x, y, z = map(int, input().split())
#     new_num = []
#     if y == 0:
#         for j in range(a):
#             new_num.append(num[x-1][(j+z) % a])
#         num[x-1] = new_num
#     else:
#         for j in range(a):
#             new_num.append(num[x-1][(a + j - z) % a])
#         num[x-1] = new_num
# s = 0
# e = a
# tot = 0
# for i in range(a):
#     for j in range(s, e):
#         tot += num[i][j]
#     if i < (a // 2):
#         s += 1
#         e -= 1
#     else:
#         s -= 1
#         e += 1
#
# print(tot)

#Second solution
import sys
sys.stdin = open('input.txt')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            # pop을 하는 순간 선택된 원소는 빠지고
            # 전체가 앞으로 한 칸 이동한다.
            # append하면 맨 뒤로 붙는다.
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            # 맨 마지막것을 빼서 맨 처음에 넣는다,
            a[h-1].insert(0,a[h-1].pop())

s = 0
e = n -1
tot = 0

for i in range(n):
    for j in range(s, e+1):
        tot += a[i][j]
    if i < (n // 2):
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(tot)
