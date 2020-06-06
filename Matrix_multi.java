def ab():
    b=int(input())
    t=[]
    for i in range(0,b):
        t.append([])
        for j in range(0,b):
            t[i].append(0)
    n=b
    c=list(map(int,input().split()))
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            p=10000000000
            for k in range(i,j):
                temp=t[i][k]+t[k+1][j]+c[i-1]*c[k]*c[j]
                if(p>temp):
                    t[i][j]=temp
    print(t[1][n-1])



for i in range(0,int(input())):
    ab()
