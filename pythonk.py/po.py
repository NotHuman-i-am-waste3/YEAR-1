'''
from queue import PriorityQueue
pipes = PriorityQueue()
n = int(input());sum=0
for i in range(n):
    pipes.put(int(input()))
while pipes.qsize()>1:
    p1=pipes.get()
    p2=pipes.get()
    sum+=p1+p2

    pipes.put(p1+p2)
if n>1:
    print(sum)
else:
    print(pipes.get())'''
n=int(input())
l=[]
for i in range(n):
     l.append(int(input()))
l1=sorted(l)
s=0
for i in range(n):
    if len(l1)>3:
       a=l1[-1]+l1[-2]
       l1.remove(l1[-1])
       l1.remove(l1[-2])
       l1.append(a)
       s=s+a
    '''if len(l1)<=3:
      if len(l1)==3:
        a=l1[0]+l[1]
        l1.remove(l1[1])
        l1[0]=a
      elif len(l1)==2:
          a=l[0]+l[1]
          l1.remove(l1[0])
          l1.remove(l1[1])
          l1.append(a)
      elif len(l1)==1:
          break'''
        
print(s)

