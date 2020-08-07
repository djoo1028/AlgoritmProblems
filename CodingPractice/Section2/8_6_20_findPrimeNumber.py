'''
Find the prime number in range

If user type 20 then find the number of primes in the range 1 to 20

'''
# This code is working but time limit exceeded
# def isPrime(n):
#     cnt = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             cnt += 1
#     if cnt == 2:
#         return True
#     else:
#         return False
#
# a = int(input())
# list_prime = []
# for i in range(2, a+1):
#     check = isPrime(i)
#     if check == True:
#         list_prime.append(check)
# print(len(list_prime))
#

# Solution2
# Sieve of Eratosthenes
# a = int(input())
# ch = [0] * (a+1)
# cnt = 0
# for i in range(2, a+1):
#     if ch[i] == 0:
#         cnt += 1
#         for j in range(i, a+1, i):
#             ch[j] = 1
#
# print(cnt)

a = int(input())
ch = [0] * (a+1)
cnt = 0
for i in range(2, a+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, a+1, i):
            ch[j] = 1
print(cnt)
