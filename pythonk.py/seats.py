m=int(input())
n=int(input())
p=int(input())
q=int(input())
li=[]
for i in range(m):
    a=list(map(int,input().split()))
    li.append(a)
l=list(map(int,input().split()))
print(li)
col=[]
for i in range(n):
    colum=[]
    for j in range(m):
        colum.append(li[j][i])
    col.append(colum)
print(col)
r=[];c=[]
for i in range(m):
    if len(set(li[i]))==1 and l==list(set(li[i])):
        r.append(i+1)
for i in range(n):
    if len(set(col[i]))==1 and l==list(set(col[i])):
        c.append(i+1)
print(r)
print(c)
if len(r)!=0 and len(c)!=0:
    for i in r:
        for j in c:
            print(i,j)
        print()
else:
    print('No winner')
