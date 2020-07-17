'''
the minimum number of change

We have enough change in 500, 100, 10

For example, if the cost was 380 then you will get 620.

620 consist of one 500, one 100, and two 20. So the total number of change is 4.

'''
#
x = int(input())
y = 1000 - x
'''
380 => 1000 - 380 -> 620

620 % 500 -> 120

120 % 100 -> 20

'''
#First thought => make every cases
# 500
five_hundred = int(y / 500) # 1
five_remainder = y % 500 # 120
# 100
one_hundred = int(five_remainder / 100) # 1
one_remainder = five_remainder % 100 # 20
# 50
fifty = int(one_remainder / 50)
fifty_remainder = one_remainder % 50
# 10
ten_decimal = int(fifty_remainder / 10)
ten_remainder = five_remainder % 10
# 5
five_decimal = int(ten_remainder / 5)
five_remainder = ten_remainder % 5
# 1
one_decimal = int(five_remainder / 1)
one_remainder = five_remainder % 1
print('500 : ',five_hundred)
print('100 : ',one_hundred)
print('50 : ',fifty)
print('10 : ',ten_decimal)
print('5 : ',five_decimal)
print('1 : ',one_decimal)

print(five_hundred + one_hundred + fifty + ten_decimal + five_decimal + one_decimal)

# Make a list and divide each element
# x = int(input())
# y = 1000 - x
# z = [500, 100, 50, 10, 5, 1]
# cnt = 0
# for i in range(len(z)):
#     if y == 0:
#         break
#     print(z[i], cnt)
#     cnt += y // z[i]
#
#     y %= z[i]
# print(cnt)
#
