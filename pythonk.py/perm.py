from itertools import combinations
n=input()
k=int(input())
s=list(n)
l=[]
for i in combinations(s,len(n)-(len(n)-k)):
   l.append(''.join(list(i)))
   print(''.join(list(i)))
for i in sorted(l):
    print(i)
