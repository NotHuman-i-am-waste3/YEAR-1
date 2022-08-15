n=input()
s=int(input())
l=[]
d=len(n)//s
l=[];l1=[];fl=[]
for i in n:
    l.append(i)
print(l)
for i in range(s):
    il=[]
    for j in range(i,len(n),s):
        il.append(l[j])
    l1.append(il)
    for k in il:
        fl.append(k)
print(l1)
print(fl)
'''p = list(input())
n = int(input())
print(p)
final = [];final1 = [];a = 0
for j in range(n):
    temp = []
    for i in range(a,len(p),n):
        temp.append(p[i])
    final.append(temp)
    a = a + 1
print(final)
for i in final:
    for j in range(len(i)):
        final1.append(i[j])
print(final1)'''

