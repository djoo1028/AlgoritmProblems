'''
If input is same as backward
then print 'Yes' if not print 'No
input example:
5
level
moon
abcba
soon
gooG

output example
#1 YES
#2 NO
#3 YES
#4 NO
#5 YES
'''
#a = int(input())


# #Solution 1
# for x in range(a):
#     letter = input()
#     reverse = letter[::-1]
#     if letter.lower() == reverse.lower():
#         print('Yes')
#     else:
#         print('No')

# # solution 2
# let = []
# for x in range(a):
#     let.append(input())
#
# for x in range(len(let)):
#     chr = let[x]
#     chr_reverse = chr[::-1]
#     if chr.lower() == chr_reverse.lower():
#         print('#{0} YES'.format(x+1))
#     else:
#         print('#{0} NO'.format(x+1))

# Teacher Solution
n = int(input())
for i in range(n):
    s = input()
    # all strings change to capital
    s = s.upper()
    # size of letter
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print('#%d NO' %(i+1))
            break
    else:
        print('#%d YES' % (i + 1))
