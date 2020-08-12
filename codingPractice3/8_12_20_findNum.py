'''
숫자만 추출
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다.
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다. 만약 “t0e0a1c2h0er”에서 숫자만 추출하면
0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다.
출력은 120를 출력하고, 다음 줄에 120 의 약수의 개수를 출력하면 됩니다. 추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
▣ 입력설명 첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.
▣ 출력설명 첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.
▣ 입력예제 1
g0en2Ts8eSoft
▣ 출력예제 1
28 <- 숫자
6 <- 약수의 갯수

'''
# Solution 1
# # Receive input like g0en2Ts8eSoft (String and digits are combined)
# a = input()
# # Empty list to put numbers
# num = []
# for i in range(len(a)):
#     # If there are numbers add to list
#     if a[i].isdigit():
#         num.append(a[i])
# digit = ''
#
# #Combine numbers in one integer
# for i in range(len(num)):
#     digit += num[i]
#
# #String to integer
# final_num = int(digit)
#
# # Count how many divisor are exist
# cnt = 0
# for i in range(1,final_num+1):
#     if final_num % i == 0:
#         cnt += 1
#
# print(final_num)
# print(cnt)


# Solution2
s = input()
res = 0
for x in s:
    if x.isdecimal():
        # 첫번째자리 0 무시하는 방법
        res = res*10+ int(x)

print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
