a=int(input())
b=int(input())
while b!=0:
  d=a&b
  a=a^b
  b=d<<1
print(a)