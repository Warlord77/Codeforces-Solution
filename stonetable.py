
from collections import Counter
n = raw_input()
r = raw_input()
p = map(str, r.split())
q = ['R', 'G', 'B']
count = 0 
r = p.[0]
for x in r[1:]:
    if x == q:
       count +=1
    else: 
       q == x
print count