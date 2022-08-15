'''s=input()
n='';l=[]
for i in s :
     if i.isdigit():
        n=n+str(i)
print(n)
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        if n[i:j] in s:
            l.append(int(n[i:j]))
print(max(l))

a=[]
b=''
for i in input():
    if i.isdigit():
        b+=i
        print(b)
    else:
        a.append(int(b))
        b=''
a.append(int(b))
print(a)
print(max(a))'''
'''s = input ()
List = []
i = 0
c = 1
while True:
    if c > len (s):
        break
    elif (i + c) > len (s):
        i = 0
        c = c + 1 
    else:
        x = 0
        Sub = s[i : (i + c)]
        digit = [range (10)]
        for ch in Sub:
            if ch.isdigit ():
                x = x + 1
        if x == len (Sub):
            List.append (int (Sub))
        i = i + 1
print (max (List))
'''

n=input().strip()
lno=[];ldigu=[];ldigl=[];ly=[]
if ' ' in n:
    print('invalid')
    exit()
if len(n)>=10 and len(n)<=12:
    for i in n:
        if i.isdigit():
            lno.append(i)
        if i.isalpha() and i.isupper():
            ldigu.append(i)
        if i.isalpha() and i.islower():
            ldigl.append(i)
        if i in ['@','$','!','%','#']:
            ly.append(i)
    if len(lno)!=0 and len(ldigu)!=0 and len(ldigl)!=0 and len(ly)!=0:
        print('valid and strong')
    else:
        print('invalid')
if len(n)>=6 and len(n)<=9:
    for i in n:
        if i.isdigit():
            lno.append(i)
        if i.isalpha():
            ldigu.append(i)
    if len(lno)!=0 and len(ldigu)!=0:
         print('valid and weak')
    else:
        print('invalid')

