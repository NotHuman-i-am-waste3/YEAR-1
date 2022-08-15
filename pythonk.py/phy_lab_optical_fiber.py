import math as m
NA=[]
W=[int(i) for i in input("W=").split()]
L=[int(i) for i in input("L=").split()]
mna,ma=0,0
for i in range(len(W)):
    sina =W[i]/m.sqrt(4*m.pow(L[i],2)+m.pow(W[i],2))
    mna=mna+sina
    NA.append(sina)
a=[]
for i in range(len(W)):
    a1=m.degrees(m.asin(NA[i]))
    ma=ma+a1
    a.append(a1)
print("NA",NA)
print("a",a)
print("mean of NA",mna/len(NA))
print("mean of a",ma/len(a))