'''
Cutting cable
We have K cables but We want to make N cables with same length by using K cable.
Find the maximum length of cable to make N cables.

input example
4 11
802
743
457
539
output example


'''

# import sys
# sys.stdin = open('input.txt')

def check(a):
    cnt = 0
    for i in num:
        cnt += ((i // a))
    return cnt

# a = the number of cable
# b = the number of cable that I want to make
a,b = map(int, input().split())
num = []




for _ in range(a):
    x = int(input())
    num.append(x)

rt = max(num)
lt = 1
res = 0
while lt <= rt:
    mid = (lt + rt) // 2

    if check(mid) >= b:
        res = mid
        lt = mid + 1

    else:
        rt = mid - 1

print(res)