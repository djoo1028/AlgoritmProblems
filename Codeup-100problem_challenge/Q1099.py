'''
find the shortest path in the map

'''
def move(x,y):
    if arr2d[x][y+1] == '1':
        if arr2d[x+1][y] == '1':
            return
        else:
            if arr2d[x+1][y] == '2':
                arr2d[x+1][y] = '9'
                return
            else:
                arr2d[x+1][y] = '9'
                move(x+1, y)
    else:
        if arr2d[x][y+1] == '2':
            arr2d[x][y+1] = 9
            return
        else:
            arr2d[x][y+1] = '9'
            move(x,y+1)


arr2d = []
for i in range(10):
    arr2d.append(input().split())

if arr2d[1][1] == '2':
    arr2d[1][1] = '9'
else:
    arr2d[1][1] = '9'
    move(1,1)


for i in range(10):
    for j in range(10):
        print(arr2d[i][j], end = ' ')
    print('')