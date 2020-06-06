import sys
t=[]
for i in range(0,11):
    t.append([])
    for j in range(0,51):
        t[i].append(-1)
def solve(e,f):
    if(f==0 or f==1 ):
        return f
    if( e==1):
        return f
    if(t[e][f]!=-1):
        return t[e][f]
    p=sys.maxsize
    for k in range(1,f+1):
        temp=max(solve(e-1,k-1),solve(e,f-k))+1
        p=min(p,temp)
    t[e][f]=p
    return p
def ab():
    b,c=map(int,input().split())
    print(solve(b,c))
    
    

for i in range(0,int(input())):
    ab()
