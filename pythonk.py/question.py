'''
s1=input()
s=input()
a=1
for i in s1:
    for j in s:
        if (i.isdigit() and j.isdigit()) or (i.isalpha() and j.isalpha()):
            a=0
if a==1:
    print('invalid')
    exit()            
if s1[0] in s:
   l=[s.index(s1[0])]
li=[]
for i in s1:
    if i in s[l[-1]:]:
        li.append(i)
        l.append(s[l[-1]:].index(i)+l[-1])
    else:
        print('false')
        exit()
if len(li)==len(s1):
    print('true')
'''
s1 = input ()
s2 = input ()
if s1.isnumeric () == True and s2.isnumeric () == False:
    print ("Invalid")
elif s1.isnumeric () == False and s2.isnumeric () == True:
    print ("Invalid")
else:
    c = 0
    def check (c):
        try:
            if c == len (s1) - 1:
                print ("true")
            else:
                ch = s1[c]
                ch1 = s1[c + 1]
                x = s2.index (ch)
                y = s2.index (ch1, x + 1)
                if x < y:
                    check (c + 1)
        except:
            print ("false")
    check (c)




    


