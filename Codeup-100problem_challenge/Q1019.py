'''
When user type 2013.8.15 then output is 2013.08.15
That means if I have one digit then add 0 in the beginning of one digit number

'''

x = input();
x = x.split('.');
yyyy = x[0].zfill(4)
mm = x[1].zfill(2)
dd = x[2].zfill(2)

print('{}.{}.{}'.format(yyyy, mm, dd))
