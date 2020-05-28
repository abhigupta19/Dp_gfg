
def ab():
    n=int(input())
    we=int(input())
    p=list(map(int,input().split()))
    w=list(map(int,input().split()))
    t=[]
    for i in range(0,n+1):
        t.append([])
        for j in range(0,we+1):
            t[i].append(0)
    for i in range(1,n+1):
        for j in range(1,we+1):
            if(w[i-1]<=j):
                t[i][j]=max(p[i-1]+t[i-1][j-w[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    print(t[-1][-1])
    



for p in range(0,int(input())):
    ab()
