n=int(input())
l=list(map(str,input().split()))
l1=[]
for i in l:
    m=max(i)
    ind=i.index(m)
    lis=list(i)
    lis.insert(ind,int(m)*m)
    l1.append(''.join(lis))
for i in sorted(l1):
    print(i,end=' ')
