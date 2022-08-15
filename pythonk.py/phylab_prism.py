
def add(MSR,VSC,LC):
    msr_deg=MSR//1
    msr_min=(MSR%1)*60  
    VSR=VSC*LC
    TR_min=VSR+msr_min
    if TR_min>=60:
        x=TR_min//60
        y=TR_min%60
        msr_deg+=x
        ans=(msr_deg,y)
    else:
        ans=[msr_deg,TR_min]
    return ans
# a,b,c=float(input()),float(input()),float(input())
# print(func(a,b,c))
def sub(DR,RR):
    if DR[1]<RR[1]:
        DR[1]+=60
        y=DR[1]-RR[1]
        DR[0]-=1
        x=DR[0]-RR[0]
    else:
        y=DR[1]-RR[1]
        x=DR[0]-RR[0]
    return [x,y]
# print(sub([180,15],[142,20]))
n=int(input('enter no of colours: '))
print('enter lc')
lc=float(input())
print('enter data of direct ray: ')

x1,y1=map(float,input().split())
x2,y2=map(float,input().split())
Total_reading_DR=[]
Total_reading_DR.append(add(x1,y1,lc))
Total_reading_DR.append(add(x2,y2,lc))
print('total reading for 1st vernier of direct ray',Total_reading_DR[0])
print('enter data of right vernier_refracted ray,msr,vsr separated by spaces: ')
right,left=[],[]
difference,ans=[],[]
tr1=[]
for i in range(n):
    x,y=map(float,input().split())
    Total_reading_right=add(x,y,lc)
    a=sub(Total_reading_DR[0],Total_reading_right)
    ans.append(a)
    b=[x1,y1]
    c=sub(b,[x,y])
    difference.append(c)
    tr1.append(Total_reading_right)
print('total reading for 1st vernier of Refracted ray',tr1)

print('difference of DR and RR',difference)
print('difference between TR of DR and RR',ans)

print('enter data of left vernier_refracted ray,msr,vsr separated by spaces: ')
difference1,ans1=[],[]
tr2=[]
print('total reading for 2st vernier of direct ray',Total_reading_DR[1])
for i in range(n):
    x,y=map(float,input().split())
    Total_reading_left=add(x,y,lc)
    a=sub(Total_reading_DR[1],Total_reading_left)
    ans1.append(a)# differnce between TR of DR and RR
    b=[x2,y2]
    c=sub(b,[x,y])
    difference.append(c)# difference between MSR AND VSR of DR AND RR
    tr2.append(Total_reading_left)
print('total reading for 2st vernier of rr', tr2 )

print('difference of DR and RR',difference)
print('difference between TR of DR and RR',ans1)
lis=[]
for i in range(n):
    a=float(ans[i][0])+float((ans[i][1])/60)
    b=float(ans[i][0])+float((ans[i][1])/60)
    c=(a+b)/2
    lis.append(c)
print('mean of vernier both verniers ',lis)
import math as m
def refind(l):
    ans=[]
    for i in l:
        a=(m.sin(m.radians((60+i)/2)))/m.sin(m.radians(30))
        ans.append(a)
    return ans
print('the refractive indexes are ',refind(lis))
