w=input().lower()
pre=[chr(x) for x in range(97,110)]
post=[chr(x) for x in range(110,123)]
print(pre,post)
z=list(zip(pre,post))
print(z)
right=1;left=0
while right<len(w):
    if ord(w[0])>110:
        print("Lost")
        break
    else:
        pos=ord(w[0])-97
        if z[pos][1]==w[right]:
            continue
        else:
            if left==0:
                w[right]==w[len(w)-1]
            else:
                ind=w.index(w[right])