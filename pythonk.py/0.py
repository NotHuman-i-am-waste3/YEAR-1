n=input()
l=list(n)
for i in  range(len(n)):
   #print(l)
   l[i-1]=l[i]  
   print(l)  