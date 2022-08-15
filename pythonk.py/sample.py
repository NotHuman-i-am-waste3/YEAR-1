n = int(input())
data = []
left=['d','f']
right=['j','k']
time=2
ans=0
cur_hand = ''
def hand(i,left):
    if i in left:
        return'left'
    else:
        return'right'
for i in range(n):
    b = input()
    cur_hand=hand(b[0],left)
    for i in b[1::]:
        if (i in left and cur_hand=='left') or (i in right and cur_hand=='right'):
            time+=4
        else:
            time+=2
            cur_hand=hand(i,left)
    if b in data:
        ans+=time//2
    else:
        ans+=time
    data.append(b)
    time=2
    print(ans)
print(ans)
