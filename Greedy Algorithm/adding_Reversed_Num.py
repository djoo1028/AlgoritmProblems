'''
The input consists of N cases. The first line of the input contains only positive integer N.

Then follow the cases. Each case consists of exactly one line with two positive integers separated by space.

These are the reversed numbers you are to add. Two integers are less than 100,000,000.
    
'''

# Decide how many input we will be received
x = int(input())

for i in range(x): # iterate 
    a, b = input().split()
    reverse_a = a[::-1] # reversed first input
    reverse_b = b[::-1] # reversed second input
    reverse_a = int(reverse_a) # When user type number it is string type so 
    reverse_b = int(reverse_b) # if we want to calculate we have to convert to integer
    result = reverse_a + reverse_b # calculation
    result = str(result)[::-1] # reverse result of sum
    reuslt_final = int(result) # convert to integer to remove zero when zero leads the result
    #reuslt_final = result.strip('0') # this is another option when zero leads number
    print(reuslt_final)
