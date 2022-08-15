from itertools import combinations as c
n = int(input())
d = {}
for _ in range(n):
    l = list(map(int,input().split()))
    for i in l:
        if i<=0:
            print('invalid input')
            exit()
    d[l[0]] = set(l[1:])
cid = list(d.keys())
carts = list(d.values())
commoncid = list(c(cid,2))
common = []
for i in list(c(carts,2)):
    common.append(i[0].intersection(i[1]))
try:
    m = len(max(common))
except ValueError:
    print(*cid)
    print(*carts[0])
    print(len(carts[0]))
    exit()
res = []
for i in range(len(common)):
    if len(common[i]) == m:
        res.append(commoncid[i])
x = []
for i in res:
    for j in range(2):
        x.append(i[j])        
if m==0:
    print('no winners')
    exit()
print(*x)
print(*max(common))
print(m)