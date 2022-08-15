D=[float(i) for i in input("enter data of D: ").split()]
d=[float(i) for i in input("enter data of 2L: ").split()]
L=[]
for i in range(len(d)):
    L.append(d[i]/2)
ta=[]
import math
for i in range(len(L)):
    ta.append(round(L[i]/D[i],3))
theta=[]
for i in range(len(D)):
    theta.append(round(math.degrees(math.atan(L[i]/D[i])),3))
si=[]
for i in theta:
    si.append(round(math.sin(math.radians(i)),3))
s=0
for i in range(len(si)):
    s=s+si[i]
mean=round((s/len(si)),3)
print("D=",D)
print("2L=",d)
print("L=",L)
print("tangent of theta=",ta)
print("theta",theta)
print("sine of theta=",si)
print("mean sin theta=",mean)
w=float(input("wavelength in nm: "))
n=int(input("order: "))
N=[]
for i in si:
    N1=round((i*(10 ** 9))/(n*w*39.37),3)
    N.append(N1)
print("no of lines per inch individual=",N)
S2=0
for i in range(len(N)):
    S2=S2+N[i]
MEANofN=S2/len(N)
print("mean no of lines per inches using only mean sin theta= ",(mean* (10 ** 9))/(n*w*39.37))
print("mean no of lines per inches= ",MEANofN)