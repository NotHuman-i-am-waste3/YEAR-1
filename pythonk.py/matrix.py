'''n=int(input());l=[];l1=[];m=[]
for i in range(n*n):
    r=input()
    l.append(r)
print(l);a=l[0]
for i in range(0,len(l),n):
    l1.append(l[i:i+n])

print(l1)
for i in range(0,len(l1[0])-2,2):
    l1[0][i]=l1[0][i+2]
if n%2==0:
    l1[0][-2]=l1[1][-1]
else:
    l1[0][-1]=l1[2][-1]

if n%2==0:
    for i in range(1,n-2,2):
        l1[i][-1]=l1[i+2][-1]
 
    l1[n-1][-1]=l1[n-1][-3]

else:
    for i in range(2,n-2,2):
        l1[i][-1]=l1[i+2][-1]

    l1[n-1][-1]=l1[n-1][-3]
for i in range(3,n-1):
    l1[-1][-i]=l1[-1][-i-2]
if n%2==0:
    l1[-1][1]=l1[-2][0]
else:
   l1[-1][0]=l1[-3][0]
if n%2==0:
    for i in range(2,n-2,2):
        l1[-i][0]=l1[-i-2][0]
else:
    for i in range(3,n-2,2):
        l1[-i][0]=l1[-i-2][0]
l1[-(n-2)][0]=a
print(l1)
for i in l1:
    print(*i)

'''
n=int(input())
x=[]
for i in range(n):
    y=[]
    for j in range(n):
        y.append(int(input()))
    x.append(y)
cor=[]
for j in range(n):
    cor.append(x[0][j])
for i in range(1,n):
    cor.append(x[i][n-1])
for j in range(n-2,-1,-1):
    cor.append(x[n-1][j])
for i in range(n-2,0,-1):
    cor.append(x[i][0])
print(cor)
for i in range(2,len(cor),2):
    cor[i],cor[i-2]=cor[i-2],cor[i]
print(cor)
c=0
for j in range(n):
    x[0][j]=cor[c]
    c+=1
for i in range(1,n):
    x[i][n-1]=cor[c]
    c+=1
for j in range(n-2,-1,-1):
    x[n-1][j]=cor[c]
    c+=1
for i in range(n-2,0,-1):
    x[i][0]=cor[c]
    c+=1
for i in range(n):
    for j in range(n):
        print(x[i][j],end="\t")
    print()
