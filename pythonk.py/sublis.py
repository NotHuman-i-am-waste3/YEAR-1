l=list(map(int,input().split()))
a=1
for i in range(len(l)):
    a=1
    print()
    for p in range(len(l)):
      for j in l[i:a]:
         print(j,end=' ')    
         a=a+1

