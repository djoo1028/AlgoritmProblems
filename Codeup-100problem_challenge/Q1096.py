'''
2d array
first : how many coordinates you are going to type
second : type location
'''

# # first answer
# x = int(input())
#
# y = [[0 for col in range(20)] for row in range(20)]
#
#
# for i in range(x):
#     a, b = input().split()
#     y[int(a)-1][int(b)-1] = 1
#
# for i in range(19):
#     for j in range(19):
#         print(y[i][j], end = ' ')
#     print('')

#Second thought
m = []
for i in range(20):
    m.append([])
    for j in range(20):
        m[i].append(0)

n = int(input())
for i in range(n):
    x,y = input().split()
    m[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1,20):
        print(m[i][j], end = ' ')
    print('')