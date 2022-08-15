n=int(input())
lis=[];lor=[]
for i in range(n):
    l=list(map(str,input().split()))
    lor.append(l)
    for i in l:
        lis.append(i)
#print(lis)
cou=[]
for i in lis:
   if lis.count(i)==1:
       cou.append(i)
#print(cou)
st=[];ans=[]
for i in lor:
    for j in cou:
        if i[0]==j:
            st.append(i[1])
            ans.append(i[0])
#print(lor)
#print(ans)
while True:
 for i in lor:
    if i[0]==st[-1]:
        st.append(i[1])
 if len(st)==len(lor)-1:
    break
#print(st)
for i in st:
    ans.append(i)
#print(ans)
for i in ans:
    print(i,end=' ')
    