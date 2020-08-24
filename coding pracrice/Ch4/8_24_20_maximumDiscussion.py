'''
We are going find the maximum number of booking meeting room
meeting time can't be conflicted. Find the maximum number of booking
first input
5 -> number of meeting
1 4 -> meeting period. First digit is starting time and second digit is end time
2 3
3 5
4 6
5 7

output
3
because (2,3), (3,5), (5,7)
'''
#
# n = int(input())
#
# meeting = []
# for i in range(n):
#     s, e = map(int, input().split())
#     # 튜플 형태로 출력가능
#     # 리스트는 출력이 안됨
#     meeting.append((s,e))
# # 그냥 이렇게 적게되면 앞에 자료에 의해서 정렬된다.
# #meeting.sort()
# # 아래와 같이 작성하면 뒤 함수 값 기준으로 정렬한다.
# meeting.sort(key = lambda x : (x[1], x[0]))
#
# et = 0
# cnt = 0
#
# for s,e in meeting:
#     if s >= et:
#         et = e
#         cnt += 1
#
# print(cnt)
import sys
sys.stdin = open('input.txt')
a = int(input())
num = []
for i in range(a):
    s,e = map(int, input().split())
    num.append((s,e))


num.sort(key = lambda x: (x[1],x[0]))

cnt = 0
ep = 0

for s,e in num:
    if s >= ep:
        cnt += 1
        ep = e

print(cnt)