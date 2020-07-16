'''
The input consists of N cases. The first line of the input contains only positive integer N.

Then follow the cases. Each case consists of exactly one line with two positive integers separated by space.

These are the reversed numbers you are to add. Two integers are less than 100,000,000.
    
'''

x = int(input())

for i in range(x):
    a, b = input().split()
    reverse_a = a[::-1]
    reverse_b = b[::-1]
    reverse_a = int(reverse_a)
    reverse_b = int(reverse_b)
    result = reverse_a + reverse_b
    result = str(result)[::-1]
    reuslt_final = int(result)
    #reuslt_final = result.strip('0')
    print(reuslt_final)
