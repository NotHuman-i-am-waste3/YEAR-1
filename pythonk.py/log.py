n = int (input ())
List = []
for i in range (n):
    x = input ().split ()
    List.append (x)
print(List)
i = 0
J = []
while i < len (List):
    x = List[i][0]
    k = False
    for j in range (len (List)):
        if x == List[j][1]:
            k = True
            i = i + 1
            break
    if k == False:
        J.append (List[i])
        List.pop (i)
        i = 0
print(J)
print (J[0][0], J[0][1], end = " ")
for i in range (1, len (J)):
    print (J[i][1], end = " ")
