'''r,c=map(int,input().split());l=[]
for i in range(r):
    a=list(map(int,input().split()))
    l.append(a)
a=0
b=c-1
#u=c//2

for i in range(r):
    for j in range(c):
        if i==j:
            print(l[i][j],end='')
        elif i==a and j==b:
            print(l[i][j],end='')
            a=a+1
            b=b-1
        else:
            print('*',end='')
    print()
#elif r%2==0 and c%2!=0 and r<c:
#      if c/r>=1.5:
'''
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
ans = [['*' for _ in range(m)] for _ in range(n)]
a = b = m // 2
for i in range(n - 1, -1, -1):
    if (a >= 0 and b <= m):
        ans[i][a] = mat[i][a]
        ans[i][b] = mat[i][b]
        a -= 1
        b += 1
for i in ans:
    for j in i:
        print(j, end=' ')
    print()