import re
n=int(input());l=[]
for i in range(n):
    a=input()
    if re.match('^[_][0-9]+[a-zA-Z][^0-9]*$',a):
        l.append('VALID')
    else:
        l.append("INVALID")
for i in l:
     print(i)
    










