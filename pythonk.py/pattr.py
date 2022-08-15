n=int(input())
a=n-1;b=0
l=[[' ' for i in range(n)] for j in range(n//2+1)]
for i in range(n):
    for j in range(n):
      if a>=0 and b<=(n//2):
        l[i][b]='*'
        l[i][a]='*'
       
    a=a-1;b=b+1
ans1=[]
ans1.append(l[1])
ans=ans1+l
ans[2][n//2-1]='*'
ans[2][n//2-1]='*'
ans[3][n//2]='*'
print(ans[0])
for i in ans:
   for j in i:
       print(j,end='')
   print()
