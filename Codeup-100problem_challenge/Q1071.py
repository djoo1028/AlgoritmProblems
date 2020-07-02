'''
repeating until user type 0
if not print whatever integer user typed and repeating

'''
x = input().split()
for i in range(len(x)):
    if x[i] == '0':
        break
    else:
        print(x[i])
