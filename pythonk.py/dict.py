
n=int(input());d={}
l=[]
l1=[]

for i in range(n):
    k=input()
    v=int(input())
    d.update({k:v})
a=input()
key_list = list(d.keys())
val_list = list(d.values())
print(val_list)
print(d[a])
for i in range(len(val_list)):
    if d[a]==val_list[i]:
         l.append(i)
print(len(l))
for i in l:
    l1.append(key_list[i])
f={d[a]:l1}
print(f)

