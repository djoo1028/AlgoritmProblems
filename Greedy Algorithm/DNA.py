'''
find hamming distance and DNA which has the smallest hamming distance
'''
# two values
# x is how many DNA will be typed
# y is size of DNA
x,y = map(int,input().split())
# Empty list
dna = []
# Empty string
result = ''
hamming_D = 0

for i in range(x):
  dna.append(input())

for i in range(y):
  # Becuase we have four dna stem which are ACGT
  count = [0,0,0,0]
  # check each column
  for j in range(x):
    if dna[j][i] == 'A'
      count[0] += 1
    elif dna[j][i] == 'C'
      count[1] += 1
    elif dna[j][i] == 'G'
      count[2] += 1
    elif dna[j][i] == 'T'
      count[3] += 1
  # Find the largest value in the cnt list
  # To find the letter and calculate Hamming distance
  largest_num = max(cnt)
  #find the location in the cnt list
  idx = cnt.index(largest_num)
  if idx == 0:
    result += 'A'
  elif idx == 1:
    result += 'C'
  elif idx == 2:
    result += 'G'
  elif idx == 3:
    result += 'T'
  hamming_D += x-largest_num
print(result)
print(hamming_D)
