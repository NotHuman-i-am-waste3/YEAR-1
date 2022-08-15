n=int(input())
d={}
for i in range(n):
    k=input()
    v=input()
    d[k]=v
search=input()
gu=d[search]
print('The name of the',search,'train is',gu,'and available for all the weekdays')