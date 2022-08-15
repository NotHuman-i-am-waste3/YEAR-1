s1=input()
s2=input()
n=int(input());l=[]
l.append(s1)
l.append(s2)
for j in range(n):
  s=''
  for i in range(0,len(s1)-1,2):
    s=s+chr(ord(s1[i])+1)
    s=s+chr(ord(s2[i+1])+1)
  l.append(s)
  if 'z' in s: 
   s=s.replace('z',chr(96))
  s1=s2
  s2=s
  #if 'z' in s2: 
  # s2=s2.replace('z',chr())
#print(l)
print(l[int(n-1)])
