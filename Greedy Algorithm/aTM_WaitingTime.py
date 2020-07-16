# Decide how many values it will take in
x = int(input())
arr = list(map(int, input().split())) # Convert all input as integer
arr_1 = arr[:x] # slice the list by user define range
arr_1.sort() # sort numbers ascending order
result = 0
final = [] 
for i in range(len(arr_1)):
    result += arr_1[i] # add numbers in the list
    final.append(result) # put result in the range

print(sum(final)) # calculate the minimum waiting time.
