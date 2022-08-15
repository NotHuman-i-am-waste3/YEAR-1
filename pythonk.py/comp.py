a=[1,2,3,4,5,6]
b=[]
for i in a:
    for j in a:
        if i!=j:
            b.append(i)
print(b)