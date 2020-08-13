'''
There is sequence which consist of the number of N.

find the number of possibility to make number M

example of input

8 3 < - 8 is the number of sequence. 3 is the number we have to make.
1 2 1 3 1 1 1 2

example of output
5

'''
a,b = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0
tot = num[0]
lt = 0
rt = 1

while True:
    if tot < b:
        if rt < a:
            tot += num[rt]
            rt += 1
        else:
            break
    elif tot == b:
        cnt += 1
        tot -= num[lt]
        lt += 1

    else:
        tot -= num[lt]
        lt += 1

print(cnt)