'''
if there are two list with ascending order

then combine two list to one list

input example
3
1 3 5
5
2 3 6 7 9
output example
1 2 3 3 5 6 7 9
'''
# import sys
# sys.stdin = open('input.txt')

n =  int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))
c = []
p1 = p2 = 0

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1

    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]

if p2 < m:
    c = c + b[p2:]

# # sort time complexity is nlogn
# result = num1 + num2
# result = sorted(result)
for i in c:
    print(i, end = ' ')

