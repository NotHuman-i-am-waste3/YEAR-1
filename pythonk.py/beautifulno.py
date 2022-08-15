from itertools import combinations as c

n=int(input())
l=[ i for i in range(9,n+1) if '9' in str(i) ]
C=0
for j in range(1,6):
 for i in c(l,j):
    if sum(i)==n:
        C+=1
print(C)