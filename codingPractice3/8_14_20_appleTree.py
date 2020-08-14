'''
First input will be odd number and
create NxN matrix
then find the sum of diamond in the grid
input example
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

output example
379

'''
# import sys
# sys.stdin = open('input.txt')

a = int(input())
num = [list(map(int, input().split())) for _ in range(a)]

res = 0
s = e = (a // 2)

for i in range(a):
    for j in range(s, e+1):
        res += num[i][j]
    if i < (a//2):
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
