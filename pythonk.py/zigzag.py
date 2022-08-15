R,C=map(int,input().split())
arr=list(map(int,input().split()))
num=1
matrix=[[0 for col in range(C)] for row in range(R)]
for row in range(R):
    for col in range(C):
        if arr[num-1]:
            matrix[row][col]=num 
            arr[num-1]-=1
            if arr[num-1]==0:
                num+=1 
for row in range(R):
    if row%2==0:
        print(*matrix[row])
    else:
        print(*matrix[row][::-1])