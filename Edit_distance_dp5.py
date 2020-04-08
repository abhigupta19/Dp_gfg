def an():
    n,m=map(int,input().split())
    b,c=map(list,input().split())
    b.insert(0,0)
    n=n+1
    m=m+1
    c.insert(0,0)
    k=[]
    for i in range(0,n):
        k.append([])
        for j in range(0,m):
            k[i].append(0)
    t=0
    for i in range(0,m):
        k[0][i]=t
        t=t+1
    pp=0
    for i in range(0,n):
        k[i][0]=pp
        pp=pp+1
    for i in range(1,n):
        for j in range(1,m):
            if(b[i]==c[j]):
                k[i][j]=k[i-1][j-1]
            else:
                k[i][j]=min(k[i-1][j],k[i][j-1],k[i-1][j-1])+1    
    print(k[-1][-1])


for i in range(0,int(input())):
    an()
