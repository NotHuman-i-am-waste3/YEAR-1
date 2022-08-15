'''s1,s2=input(),input();l1,l2=len(s1),len(s2);s11,s22=0,0
if l1<l2:
    print(s1)
    s11+=1
else:
    print(s2)
    s22+=1
def pattern(s):
    start,endc=0,-1
    l=len(s)
    if l%2==0:
        r=l//2;c=l+3
        for i in range(r):
            for j in range(c):
                if i==0:
                    if j==0:
                        print(s[start],end="");start+=1
                    elif j==c-1:
                        print(s[endc],end="");endc=endc-1
                    else:
                        print("*",end="")
                else:
                    if j==i+1:
                        print(s[start],end="");start+=1
                    elif j==(c-1)-(i+1):
                        print(s[endc],end="");endc=endc-1
                    else:
                        print("*",end="")
            print()
    else:
        r=(l//2)+1;c=l+2
        for i in range(r):
            for j in range(c):
                if i==0:
                    if j==0:
                        print(s[start],end="");start+=1
                    elif j==c-1:
                        print(s[endc],end="");endc=endc-1
                    else:
                        print("*",end="")
                elif i==r-1:
                    if j==c//2:
                        print(s[c//2],end="")
                    else:
                        print("*",end="")
                else:
                    if j==i+1:
                        print(s[start],end="");start+=1
                    elif j==(c-1)-(i+1):
                        print(s[endc],end="");endc-=-1
                    else:
                        print("*",end="")
            print()


if s11==0:
    pattern(s1)
if s22==0:
    pattern(s2)
'''



s1 = input()
s2 = input()
len1 = len(s1);len2 = len(s2)
c=len1//2;f=len2//2
a=0;e=0
b=len1-1;d=len2 - 1

if len1 > len2 :
    print( s2 )
    for i in range(c+1):
        print()
        if len1%2==0 and i==c:
            break
        for j in range(len1):
            if j==a:
                print(s1[j],end=' ')
            if j==b:
                print(s1[j],end=' ')
            else:
                print(' ',end=' ')
        a += 1
        b -= 1
else:
    print( s1 )
    for i in range(f+1):
        print()
        if len2%2==0 and i==f:
            break
        for j in range(len2):
            if j==e:
                print(s2[j],end=' ')
            if j==d:
                print(s2[j],end=' ')
            else:
                print(' ',end=' ')
        e += 1
        d -= 1
    


