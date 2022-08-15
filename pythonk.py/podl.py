n = int (input ())
D = {}
for i in range (n):
    x = input ().split ()
    D[x[0]] = int (x[1])
l = list (D.values ())
k = list (D.keys ())
l1 = []
for i in range (n):
    for j in range (n):
        if i != j:
            sub = [l[i], l[j]]
            s = list (set (l) - set (sub))
            if sum (s) == (2 * sum (sub)):
                l1.append (sub)
print(l)
x = l1[0]
print (k[l.index (x[0])], k[l.index (x[1])])
for i in range (n):
    if i != l.index (x[0]) and i != l.index (x[1]):
        print (k[i], end = " ")
    