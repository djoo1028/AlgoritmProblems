'''
Q1089
series find the number
user will type a = beginning number
               d = differences
               n = location
               print(value of location n)
'''
def series(arg1, arg2, arg3):
    begin = int(arg1)
    differences = int(arg2)
    indexNum = int(arg3)

    result = 0
    for i in range(indexNum):
        result = differences * i + begin

    print(result)

'''
Q1090
'''
def geometricSequence(arg1, arg2, arg3):
    begin = int(arg1)
    mul = int(arg2)
    indeNum = int(arg3)
    result = 0
    for i in range(indeNum):
        result = begin * (mul ** i)
    print(result)

'''
Q1091
'''
def compli(arg1, arg2, arg3, arg4):
    begin = int(arg1)
    mult = int(arg2)
    add = int(arg3)
    indexNum = int(arg4)

    result = 0
    # we can set begin as a result
    # Then we will have shorter code than I have right now
    if (indexNum - 1) == 0:
        print(begin)
    else:
        for i in range(indexNum-1):
            result = begin * mult + add
            begin = result
        print(result)

#x, y, z = input().split()
#series(x,y,z)
#geometricSequence(x,y,z)




#x, y, z, w = input().split()
#compli(x,y,z,w)
