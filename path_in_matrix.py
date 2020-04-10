def ab():
    b=int(input())
    k=[]
    c=list(map(int,input().split()))
    for i in range(0,b):
        k.append([])
        for j in range(0,b):
            k[i].append(c.pop(0))
    for i in range(1,b):
        k[i][0]=k[i][0]+max(k[i-1][0],k[i-1][1])
        k[i][-1]=k[i][-1]+max(k[i-1][-1],k[i-1][-2])
        for j in range(1,b-1):
            k[i][j]=k[i][j]+max(k[i-1][j],k[i-1][j-1],k[i-1][j+1])
    
    print(max(k[-1]))
for i in range(0,int(input())):
    ab()
