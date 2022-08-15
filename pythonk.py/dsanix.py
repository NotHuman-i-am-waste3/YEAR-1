import math as m
n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
l1=int(input())
finl=[]
find=[]
for i in l:
    subl=[]
    c=m.floor(i/l1)
    for j in range(c):
        subl.append(l1)
    subl.append(i%l1)
    finl.append(subl)
    find.append(len(subl))

m=max(find)
for i in finl:
    c=m-len(i)
    for j in range(c):
        i.append(0)

finc=[]
for i in range(len(finl[0])):
    l=[j[i] for j in finl]
    finc.append(l)

indx=[]
for i in range(len(finl)):
    for j in range(len(finl[0])):
        if finl[i][j]==0:
            indx.append([j-1,i])
            break
ans=[]
for i in indx:
    d=[]
    for a in range(i[0]+1):
        if a==i[0]:
            for b in range(i[1]+1):
                d.append(finc[a][b])
            break
        for j in finc[a]:
            d.append(j)
    ans.append(sum(d))
print(ans)
