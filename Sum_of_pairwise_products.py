import numpy
from itertools import combinations_with_replacement
n=int(input("Enter the number"))
l=[]
s=0
for i in range(1,n+1):
    l.append(i)
comb = combinations_with_replacement(l,2)

for j in list(comb):
    s=s+numpy.prod(j)
print(s)
