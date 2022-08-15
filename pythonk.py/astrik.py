n=int(input())
l=[];indx=[]
for i in range(n):
    a=input()
    l.append(a)
    indx.append(len(a))
def fuck(indx,l):
   if len(indx)!=len(list(set(indx))):
       an=[]
       for i in list(set(indx)):
           le=[]
           for j in l:
               if len(str(abs(int(j))))==i :
                   le.append(int(j))
           #print(le)
           if len(le)==1 and str(le[0])[::-1]==str(le[0]):
               if len(str(le[0]))%2==0:
                   o=len(str(le[0]))//2
               else:
                   o=len(str(le[0]))//2+1
               if int(le[0])<0: 
                  a=str(le[0][0])+str(le[1:o])
                  an.append(a)
               else:
                   an.append(str(le[0])[0:o])
           if len(le)==1 and str(le[0])[::-1]!=str(le[0]):
               if int(le[0])<0: 
                 a=str(le[0])[0]+str(le[0])[1:][::-1]
               else:
                  an.append(str(le[0])[::-1])
           if len(le)>1:
               an.append(str(sum(le)))
       l=an
       ind=[]
       for i in an:
           ind.append(len(i))
       fuck(indx,l)
   else:
       print(l)

fuck(indx,l)

        

