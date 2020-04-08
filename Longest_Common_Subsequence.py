def ab():
    n,m=map(int,input().split())
    n=n+1
    m=m+1
    b=list(input())
    c=list(input())
    b.insert(0,0)
    c.insert(0,0)
    k=[]
    for i in range(0,m):
        k.append([])
        for j in range(0,n):
            k[i].append(0)
    
    
    for i in range(1,m):
        for j in range(1,n):
            if(c[i]==b[j]):
                k[i][j]=k[i-1][j-1]+1
            else:
                k[i][j]=max(k[i][j-1],k[i-1][j])
        
    print(k[-1][-1])
    






for i in range(0,int(input())):
    ab()
