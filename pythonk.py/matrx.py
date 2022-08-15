r,c=map(int,input().split())
l=[];lis=[]
for i in range(r):
    a=list(map(str,input().split()))
    l.append(a)
for i in l[0]:
    lis.append(i) 
print(lis)
for i in range(1,r-1):
    lis.append(l[i][-1])
print(lis)
for i in range(-1,-c-1,-1):
    lis.append(l[-1][i])
print(lis)
for i in range(r-2,0,-1):
    lis.append(l[i][0])
print(lis)
for i in lis:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        print(i)
        index=lis.index(i)
        break
if index>=0:
     ans=lis[index:]+lis[0:index]
     for i in ans:
            print(i,end='')
