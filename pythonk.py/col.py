r,c=map(int,input().split()) 
m=[list(map(int,input().split())) for i in range(r)] 
k=int(input())
z=[]
for i in zip(*m):
    z.append(list(i))
m=z                 
while k>0:
    l=[]
    for i in m:
        l.append([sum(i),i])
    l=sorted(l,key=lambda x:x[0])
    print(l)
    print(z)
    m.remove(l[-1][-1])
    k-=1 
for i in zip(*m):
    print(*i)