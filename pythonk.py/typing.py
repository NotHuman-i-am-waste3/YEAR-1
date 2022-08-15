'''n=int(input())
lf=['d','f'];rg=['j','k']
lis=[];dup=[];indx=[]
for i in range(n):
 l=[2]
 a=input()
 if a not in dup:
    dup.append(a)
    l1=[a[0]]
    for i in a[1:]:
        if i in lf:
            if l1[-1] in lf:
                 l.append(4)
            else:
                l.append(2)
        elif i in rg:
            if l1[-1] in rg:
                l.append(4)
            else:
               l.append(2)
        l1.append(i)
    lis.append(sum(l))
 else:
     indx.append(dup.index(a))
for i in indx:
    lis.append(int(lis[i]/2))
print(sum(lis))'''
'''time, already = 0, dict()
find_time = lambda i: 2 + sum((4 if i[k] in 'df' else 2) if i[k - 1] in 'df' else (2 if i[k] in 'df' else 4) for k in range(1, len(i)))
for i in [input() for _ in range(int(input()))]:
    time += already[i] >> 1 if i in already else find_time(i)
    already[i] = find_time(i)
print(time)'''
i=input()
l=['d','f'];r=['j','k'];s,r1=2,2;time=[]
for ch in i:
    if ch in l:
        r1=2
        time.append(s)
        s=4
    if ch in r:
            s=2
            time.append(r1)
            r1=4
    print(time)


