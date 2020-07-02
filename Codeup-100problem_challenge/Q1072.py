'''
user enter the number of integer will take in
print each integer
'''


'''
x = int(input())
a = input().split()
for i in range(x):
    print(a[i])
'''

'''
Q1073
Stop program when there is zero 
'''

a = input().split()
for i in range(len(a)):
    if a[i] == '0':
        break
    else:
        print(a[i])


