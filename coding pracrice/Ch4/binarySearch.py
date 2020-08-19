'''
binary search
find the mid point.
input example
8 32
23 87 65 12 57 32 99 81
output example
3

'''
# #solution 1
# a,b = map(int, input().split())
#
# num = list(map(int, input().split()))
#
# num.sort()
#
# print(num.index(b) + 1)
#


n,m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
lt = 0
rt = n-1

while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break

    elif a[mid] > m:
        rt = mid - 1

    else:
        lt = mid + 1
