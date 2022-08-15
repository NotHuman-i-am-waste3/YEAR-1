n=int(input())
b=bin(n)
l2=[]
l=b[2:];l1=[]
print(l)
p=l[-3:len(l)+1]

#print(type(p))
for i in str(p):
    if i=='1':
        l1.append('0')
    else:
        l1.append('1')
print(l1)
s=''
for i in l[0:len(l)-len(l1)]:
     l2.append(i)
c=l2+l1
s=''
for i in c:
    s=s+i
print(int(s,2))




