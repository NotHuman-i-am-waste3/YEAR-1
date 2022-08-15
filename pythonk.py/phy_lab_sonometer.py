from math import*
ll=[]
lF=[]
for i in range(5):
    m=float(input('mass in kg : '))
    ft=float(input('First trial: '))
    st=float(input('second trial: '))
    mu=float(input('mu with calculation: '))
    T=m*9.8
    meanc=(ft+st)/2
    meanm=((ft+st)/2)*0.01
    ll.append(meanm)
    F=(1/(4*meanm))*sqrt((T/mu))
    Fn=(1/(2*meanm))*sqrt((T/mu))
    s=1/(4*(pow(Fn,2)*(mu)))
    Fs=1/4*(1/(sqrt(mu*s)))
    lF.append(F)
    print('tension :',T)
    print('mean in (cm) is ',meanc)
    print('mean in (m) is ',meanm)
    print('l^2 : ',meanm*meanm)
    print('Frequency by formula : ',F)
    print('Frequency by slope : ',Fs)
a=sum(ll)/len(ll)
b=sum(lF)/len(lF)
print('mean of Frequency F : ',b)
print('mean of lenght L  : ',a)