'''

User will type hour:minute:sec

then print just minute.

Exception if we have the time like 06:00:00 -> it has to be printed 0 instead of 00
'''

x = input()
x_list = list(x.split(':'))

if x_list[1] == '00':
    print('0')
else:
    print(x_list[1])
