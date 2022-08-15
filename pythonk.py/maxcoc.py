s=input()
l=[]
for i in range(len(s)-1):
    a=s[i:i+2]
    k=[int(i) for i in a]
    l.append(s[0:i]+str(sum(k))+s[i+2:])
print(max(l))
