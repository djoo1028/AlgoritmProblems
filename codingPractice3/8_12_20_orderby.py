'''
There are cards from 1 to 20. Now we are going to shuffle card with certain range

If user type 5 10 then card will be shuffled in decending order from 5 to 10. 5 and 10 are inclusive.

So the results are 1,2,3,4,10,9,8,7,6,5,11,12....20.

User will type 10 times. Now we have to find the result

input example:
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20

output example
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
'''
import sys
sys.stdin = open('input.txt')

# mysolution
num = list(range(1,21))

for i in range(10):
    a,b = map(int,input().split())
    if b > a:
        size = b - a + 1
        for j in range(size // 2):
            # temp = num[(b-1)-j]
            # num[(b-1)-j] = num[(a-1)+j]
            # num[(a-1)+j] = temp
            num[(a-1) +j], num[(b-1)-j] = num[(b-1)-j], num[(a-1)+j]
for i in num:
    print(i, end = ' ')

# teacher solution
# a = list(range(21))
#
# # _는 아무 변수 없이 for loop를 돈다
# for _ in range(10):
#     s, e = map(int, input().split())
#     for i in range((e-s+1) // 2):
#         a[s+i], a[e-i] = a[e-i], a[s+i]
# # 0번 인덱스에 있는 것을 날려라
# a.pop(0)
# for x in a:
#     print(x, end = ' ')