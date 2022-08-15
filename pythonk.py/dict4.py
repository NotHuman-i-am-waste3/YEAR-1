n=input()
indx=[0];set1={};l=[];l1=[]
for i in range(len(n)):
    if n[i]==' ':
         indx.append(i+1)
for i in range(len(indx)-1):
    v=list(n[indx[i]:indx[i+1]])
    v.pop(-1)
    set1[v[0]]=''.join(v)
    l.append(''.join(v))
    l1.append(v[0])
print(l)
print(set1)
ans=[]
p=sorted(list(set(l1)))
print(p)


            





