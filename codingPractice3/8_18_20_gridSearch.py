'''



'''
import sys
sys.stdin = open('input.txt')
num = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        digit_row = num[j][i:i+5]
        if digit_row == digit_row[::-1]:
            cnt += 1

        for k in range(2):
            if num[i+k][j] != num[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)