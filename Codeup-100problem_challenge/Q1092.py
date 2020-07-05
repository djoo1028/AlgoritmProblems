'''
find LCM(Least common multiple)
among three values
'''


x,y,z = input().split()
x = int(x)
y = int(y)
z = int(z)

day = 1

while(((day % x) != 0) or ((day % y) != 0) or ((day % z) != 0)):
    print(day % x, day %y, day % z)
    day += 1
print(day % x, day %y, day % z)
print(day, 'last')