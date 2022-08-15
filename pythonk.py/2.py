r,c=map(int,input().split());l=[];m=[]
for i in range(r):
    a=list(map(str,input().split()))
    l.append(a)
for i in range(r):
    for j in range(c):
        m.append(l[i][j])
print(m)