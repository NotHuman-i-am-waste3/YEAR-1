d={}#empty dictionary
n=int(input())#no of students
for i in range(n):
    x=input().split()#name of student followed by no of ques solved resp easy medium hard separated by spaces
    totalscore=(int(x[1])*10)+(int(x[2])*30)+(int(x[3])*50)#sum of score
    if not d.get(totalscore):
        d[totalscore]=[x[0]]
       # print(d)
    else:d
        d[totalscore].append(x[0])
        #print(d)
print(d)
rank=1
score=list(d.keys())# making a list of totalscores and then sorting in descending order 
score.sort(reverse=True)
for i in score:
    studentname=d[i]#getting the list of students with a particular total score
    studentname.sort()#for alphabetical order sorting the list of names of student
    nooftimessamerank=0
    for j in studentname:
        print(rank," ",j)
        nooftimessamerank+=1
    rank+=nooftimessamerank
    