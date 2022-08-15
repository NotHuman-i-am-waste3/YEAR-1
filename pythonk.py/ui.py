n=int(input())
p=[]
for i in range(n):
    pola=[int(x) for x in input().split()]
    p.append(pola)
d={}    
print(p) 
for i in range(n):
    p[i].sort()
print(p)
for i in range(n):
    if len(p[i])<len(p[i+1]):
        for i in range(len(p[i])):
            if p[i][i]==p[1][i]:
                if p[i][i] not in d:
                    d[p[i][i]]=p[i][i]
print(d)


    