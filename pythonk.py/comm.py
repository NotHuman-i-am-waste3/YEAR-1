n=int(input())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
p=int(input())
first_elements=[];second_elements=[]
for i in range(len(l)):
    first_elements.append(l[i][0])
    second_elements.append(l[i][1])
if p in first_elements and p in second_elements:
   index=first_elements.index(p)
   index1=second_elements.index(p)
else:
    print(0)
    exit()
lis=[]
for i in range(index,index1+1):
    for j in range(index,index1+1):
        if first_elements[i]==second_elements[j]:
            lis.append(second_elements[i])
print(len(lis))
print(lis)