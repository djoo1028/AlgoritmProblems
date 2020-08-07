def digit_sum(n):
    total = 0
    num1 = []
    n = str(n)
    for i in range(len(n)):
        total += int(n[i])
    return total


a = int(input())
num = list(map(int, input().split()))
result = 0

for i in range(a):
    temp = digit_sum(num[i])
    if temp > result:
        result = temp
        final = num[i]

print(final)

