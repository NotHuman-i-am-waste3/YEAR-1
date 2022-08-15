a=input()
s='abcdefghijklmnopqrstuvwxyz'
a1=list(s)+list(s.upper())
l1=[ i for i in range(0,26)]
l2=[ i for i in range(26,26+26) ]
l=l1+l2
su=[]
for i in a:
    o=l[a1.index(i)]
    su.append(o)
print(sum(su))
c=0
for i in list(str(sum(su))):
    c=c+int(i)
print(c)
print(c*sum(su))
