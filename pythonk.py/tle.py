n=int(input())
m=int(input())
c=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if sum([int(i) for i in str(i)])!=sum([int(i) for i in str(j)]): # and (n<=i<=j<=m):
            c+=1
            print(i,j)
# a=(10**9)+7
print(c)






