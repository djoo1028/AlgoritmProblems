'''
find the Kth number
first input is the number of test case
each case we have to type N,s,e,k
N is the number of digit
s is beginning location
e is end location
K is kth number
example
2
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
'''

# My Work
num_test = int(input())

for i in range(num_test):
    list_final = []
    n,s,e,k = map(int, input().split())
    num_list = list(map(int, input().split()))
    for j in range(s,e+1):
        list_final.append(num_list[j-1])
    list_final.sort()
    print('#{}'.format(i+1), list_final[k-1])


#Solution
# T = int(input())
#
# for t in range(T):
#     n, s, e, k = map(int, input().split())
#     num_list = list(map(int, input().split()))
#     # By using slice, we can store list with certain length
#     a = num_list[s-1:e]
#     a.sort()
#     print('#{}'.format(t+1), a[k-1])
