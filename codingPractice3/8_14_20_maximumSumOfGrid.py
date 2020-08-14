import sys
sys.stdin = open('input.txt')
# # First solution
# a = int(input())
# matrix = []
# for i in range(a):
#     x = input().split()
#     c = []
#     for j in range(a):
#         c.append(int(x[j]))
#     matrix.append(c)
# com = []
# sum = []
#
# for i in range(a):
#     summation = 0
#     for j in range(a):
#         summation += matrix[i][j]
#     sum.append(summation)
# com.append(max(sum))
# sum_ver = []
#
# for i in range(a):
#     summation_ver = 0
#     for j in range(a):
#         summation_ver += matrix[j][i]
#     sum_ver.append(summation_ver)
# com.append(max(sum_ver))
#
# summation_diag = 0
# for i in range(a):
#     summation_diag += matrix[i][i]
#
# com.append(summation_diag)
# summation_diag_ver = 0
# for i in range(a):
#     summation_diag_ver += matrix[i][(a-1) - i]
#
# com.append(summation_diag_ver)
#
# print(max(com))
#


# Second Solution
a = int(input())
num = [list(map(int, input().split())) for _ in range(a)]

for i in num:
    print(i)

largest = -2147000000

for i in range(a):
    row = 0
    column = 0
    for j in range(a):
        row += num[i][j]
        column += num[j][i]
    if row > largest:
        largest = row
    if column > largest:
        largest = column

diag = 0
oppo_diag = 0
for i in range(a):
    diag += num[i][i]
    oppo_diag += num[i][(a-1) - i]

if diag > largest:
    largest = diag
if oppo_diag > largest:
    largest = oppo_diag

print(largest)