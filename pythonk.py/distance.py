s={'geeks','for','geeks','contribute','practice'};l=[]
for i in s:
    l.append(i)
w1=input()
w2=input()
print(l)
d=[];c=0
if w1 or w2  in s:
    for i in range(l.index(w1)+1,l.index(w2)):
        d.append(l[i])
    c=c+1
else:
    for i in range(l.index(w1)+1,l.index(w2)):
        d.append(l[i])
c1=0
print(d)
for i in d:
    if i in s:
        c1=c1+1
print(len(d)+c1+c)
    
    
