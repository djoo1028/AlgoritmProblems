'''
find the maximum number of swap in heap sort

'''
'''
To find the maxmimum number of swap in heap

the smallest integer which is 1 has to be located in the last spot

and the maximum value has to be located right next one

and change to parent node
'''
# Size of heap
n = int(input())

# Default size of heap
heap = [0,1]

# swap the x and y in arr
def swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

# range of heap
for i in range(2, n+1):
    # add new value into the heap array
    heap.append(i)
    # swap the value the last element and the right before the last
    # Because 1 has to be located at the last spot
    swap(heap, i, i-1)
    # This is maximum value in the heap
    # J is location
    j = i-1
    while j != 1:
        # the maximum value is located at the j
        # j has to move to the top because this is maximum heap
        # parent node has to be greater than equal to the child node
        swap(heap, j, j//2)
        j = j // 2
# print from index 1 in heap
# Because idex 0 is 0.
for i in heap[1:]:
    print(i, end = ' ')
