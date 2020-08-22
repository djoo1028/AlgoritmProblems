def check(mid):
    tot = 0
    cnt = 1
    for i in num:
        if tot + i > mid:
            cnt += 1
            tot = i
        else:
            tot += i
    return cnt

a,b = map(int, input().split())
num = list(map(int, input().split()))
maxx = max(num)
lt = min(num)
rt = sum(num)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2

    if mid >= maxx and check(mid) <= b:
        res = mid
        rt = mid - 1

    else:
        lt = mid + 1

print(res)