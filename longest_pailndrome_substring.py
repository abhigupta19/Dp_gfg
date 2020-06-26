#User function Template for python3



# you need to complete this function
def longestPalindrome(s):
    e=s[::-1]
    t=[]
    for i in range(0,len(s)):
        t.append([])
        for j in range(0,len(s)):
            t[i].append(False)
    res=0
    for i in range(0,len(s)):
        t[i][i]=True
    start=0
    max=0
    for k in range(2,len(s)+1):
        for i in range(0,len(s)-k+1):
            j=i+k-1
            if(k==2 and s[i]==s[j]):
                t[i][j]=True
                if(k>max):
                    max=k
                    start=i
            elif(s[i]==s[j] and t[i+1][j-1]):
                t[i][j]=True
                if(k>max):
                    max=k
                    start=i       
    p=""
    if(max==0):
        p=s[0]
        return p
    for i in range(0,max):
        p+=s[start]
        start+=1
    return max


#{
#  Driver Code Starts
#Initial Template for Python 3


# Driver program to test above functions

if __name__=='__main__':
    tc=int(input())
    for _ in range(tc):
        str=input()
        print(longestPalindrome(str))
# } Driver Code Ends
