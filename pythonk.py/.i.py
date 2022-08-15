n=int(input())
c=str(n)*3
l=[[1,1]];m=[]
for i in range(0,4):
    a=c[i:i+4]
    m.append(a)
    l1=[]
    for i in range(1,10000):
        if int(a)%i==0 and i!=int(a):
            l1.append(i)
    if max(l1) > l[0][1]:
        l[0]=[a,max(l1)]
print(l)
print(m)
