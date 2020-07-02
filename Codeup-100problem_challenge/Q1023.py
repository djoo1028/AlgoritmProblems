'''
if you have real number
then you will print interger in the first line
and you will print decimal in the second line
'''


x = input()
x = x.split('.')

int_x = x[0]
decimal_x = x[1]

print(int_x)
print(decimal_x)
