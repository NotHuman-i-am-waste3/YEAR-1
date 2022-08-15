
from itertools import combinations 
n=int(input());l1=[]
l=list(map(int,input().split()))
for j in range(1,len(l)+1):
   for i in combinations(l,j+1):
    if sum(i)==4:
        l1.append(list(i))
        
cv=[]
c=l.count(4)
l2=[]
print(l1)
for i in l1:
    if i not in cv:
        cv.append(i)
print(cv)
print(len(cv))
for i in cv:
    l2.append(sorted(i))
sp=[]
for i in l2:
    if i not in sp:
        sp.append(i)
print(sp)
d=len(sp)+c
s=[]
pm=[]

for i in sp:
    for j in i:
         if j not in pm:
            
             pm.append(j)
print(pm)
for i in l:
    if i  not in pm:
        s.append(i)
print(s)



