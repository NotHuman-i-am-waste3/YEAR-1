n = input()
n1=input()
def pranay(x,y):
    res=[]
    for i in x:
        if i in y:
            res.append(i)
            print(i)
    return res
a=pranay(n,n1)

print(a)