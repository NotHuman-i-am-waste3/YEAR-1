f=open('sile1.txt','w+')
for i in range(10):
    f.write('this is line %d\r\n'%(i+1))
    print(i)
f.close()

f.close()
f=open('sile1.txt','w+')
for i in range(2):
    f.write('Appended line %d\r\n'%(i+1))


f=open('sile1.txt','r')
if f.mode == 'r' :
    contents = f.read()
print(contents)

