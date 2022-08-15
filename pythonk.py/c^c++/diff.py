l1=[5,5,4,7,-5,-4,-3,-2,-1,-6]
c=0
for i in l1:
  if sum(l1)>0:
        if i>=0:
          l1[c]=(i-1)
        else:
            l1[c]=(i+1)
  if sum(l1)<0:
        if i>=0:
          l1[c]=(i+1)
        else:
            l1[c]=(i+1)
  if sum(l1)==0:
     print(l1,sum(l1))
     break
  c+=1


  
  