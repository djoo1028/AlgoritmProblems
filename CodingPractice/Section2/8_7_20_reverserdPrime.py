'''
Check reversed number is prime or not
Example of input
5
32 55 62 3700 250

Example of output
23 73
'''


def reverse(x):
    # Solution 1
    # q = str(x)
    # return int(q[::-1])

    # Solution 2
    # Using remainder
    res = 0
    while x>0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res
def isPrime(x):
    # if x != 1:
    #     for i in range(2, x):
    #         if x % i == 0:
    #             return False
    # else:
    #     return False
    #
    # return True
    if x == 1:
        return False
    for i in range(2, x //2 +1):
        if x % i == 0:
            return False
    else:
        return True

a = int(input())
num = list(map(int, input().split()))

for i in range(a):
    rev_num = reverse(num[i])
    prime = isPrime(rev_num)
    if prime == True:
        print(rev_num, end = ' ')

    # if isPrime(rev_num):
    #     print(rev_num,end = ' ')
