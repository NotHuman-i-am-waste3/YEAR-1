#n=input()
#b=n[0]
#a=n[-1]
#print(int(b)**int(a))
s=input().strip() 
#n=int(input()) 
k=len(s)//3   
l=[]
for i in range(0,len(s),k): 
        a=s[i:i+k] 
        l.append(a) 
print(l)
print(k)
if len(set(l))==1: 
    print('yes') 
else: 
   print('No')
'''
s=input();l=[];start,end=0,len(s)//3
for i in range(start,end):
    l.append(s[start:end])
    start,end=end,end+len(s)//3
if len(set(l))==1:
    print("YES")
else:
    print("NO")'''