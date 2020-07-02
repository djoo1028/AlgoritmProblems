'''

print number by each digits location
for example, if user type 75254 then print like down below
[70000]
[5000]
[200]
[50]
[4]
'''
import math


x = input()
x_list = list(x)

print('['+str(int(x_list[0]) * 10000)+']') # int can't use concatenate so I converted to str
print('['+str(int(x_list[1]) * 1000)+']')
print('['+str(int(x_list[2]) * 100)+']')
print('['+str(int(x_list[3]) * 10)+']')
print('['+str(int(x_list[4]) * 1)+']')
