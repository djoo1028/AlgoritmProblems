'''
If user type xxxxxx-xxxxxxx then print xxxxxxxxxxxxx

'''

x = input()
x = x.split('-')
begin_x = x[0]
end_x = x[1]

print(begin_x + end_x)