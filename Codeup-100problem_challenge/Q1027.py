'''
Change format
if user type yyyy.mm.dd then print with dd-mm-yyyy
'''


x = input()
x = x.split('.')
print(x);
year = x[0]
month = x[1]
day = x[2]

print(str(day) + '-' + str(month) + '-' + str(year))
