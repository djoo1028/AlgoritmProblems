'''
Decision Algorithm
We are going to locate the horse into the barn
Horses don't like to be located right next each other.
We have to find the maximum distance of between horses

First line input
5 3
5 is the number of barn and 3 is number of horses

Second line
1
2
8
4
9

the numbers are x-location of barn. We are going to put horses into barn.
We have to find the maximum distance between barn

Output
3

'''
def check(mid):
    cnt = 1
    ep = num[0]
    for i in range(1, a):
        if num[i] - ep >= mid:
            cnt += 1
            ep = num[i]
    return cnt

# a is the number of barn
# b is the number of horse
a,b = map(int, input().split())
# Empty list
num = []
for _ in range(a):
    num.append(int(input()))

num.sort()


lt = min(num)
rt = max(num)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if check(mid) >= b:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)

