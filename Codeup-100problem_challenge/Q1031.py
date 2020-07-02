'''

10Decimal to Oct

'''



x = int(input())
oct_num = oct(x)
remove_prefix = oct_num[2:]
print(remove_prefix)

#I was going to use format like down below
#And there is error like 'ValueError: Unknown format code 'o' for object of type 'str'
#print('{0:o}'.format(oct_num))


'''

decimal to hexadecimal

'''

y = int(input())
hex_num = hex(y)
remove_prefix_hex = hex_num[2:]
remove_prefix_hex = remove_prefix_hex.upper()
print(remove_prefix_hex)

'''
Octa -> decimal
'''

z = input()
decimal = int(z,8)
print(decimal)

'''
hexa to Octa

'''

z = hex(input())
z = oct(z)
print(z)

