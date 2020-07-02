'''
print alphabet by order
if user type f then print a ~ f

chr -> int -> letter
ord -> letter -> integer
a -> 97
z -> 122

'''
def order(arg1):
    a = arg1
    a = ord(a)
    loc = 0
    for i in range(97, a+1):   # i is a variable between start and end
        print(chr(i), end=' ') #when result print in a row
        i = i + 1

'''
print number util get the number
for example, user type 3 then print 0 1 2 3 in vertical

'''
def orderNum(arg1):
    a = int(arg1)
    for i in range(0, a + 1):
        print(i)
        i = i + 1

'''
add even number in range
Q1078
'''
def sumEven(arg1):
    a = int(arg1)
    sum = 0
    for i in range(a+1):
        if i % 2 == 0:
            sum = sum + i
        else:
            sum
    print(sum)

'''
Q1079
keep printing until u get 'q'
'''
def findQ(arg1):
    a = arg1.split()
    for i in range(len(a)):
        if a[i] == 'q':
            print(a[i])
            break
        else:
            print(a[i])


'''
Q1080
keep adding num until the number is greater than typed number
for example if user type 55 then it should print 10
'''

def summation(arg1):
    a = int(arg1)
    result = 0
    for i in range(1001):
        result = result + i
        #print(result)
        if result >= a:
            print(i)
            break

x = input()
#orderNum(x)
#sumEven(x)
#findQ(x)
summation(x)