r,c=map(int,input().split())
x=[]
for i in range(r):
    y=list(map(str,input().split()))
    x.append(y)
cor=[]
for j in range(c):
    cor.append(x[0][j])
for i in range(1,r):
    cor.append(x[i][c-1])
for j in range(c-2,-1,-1):
    cor.append(x[r-1][j])
for i in range(r-2,0,-1):
    cor.append(x[i][0])
for i in range(len(cor)):
    if cor[i] in 'aeiou' or cor[i] in 'AEIOU':
        print(cor[i:])
        breakni.