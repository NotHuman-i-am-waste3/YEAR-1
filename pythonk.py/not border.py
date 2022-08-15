n=int(input())
l=[ list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i!=0 and i!=n-1:
            if j!=0 and j!=n-1:
                print(l[i][j],end=' ')
    print()

