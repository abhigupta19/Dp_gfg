def ab():
	b=int(input())
	l=list(input())
	k=[]
	for i in range(0,b):
		k.append([])
		for j in range(0,b):
			k[i].append(0)
	for i in range(0,b):
		k[i][i]=1
	for j in range(0,b):
		for i in range(0,b-1):
				if(j>i):
					if(l[i]==l[j]):
						k[i][j]=k[i+1][j-1]+2
					else:
						k[i][j]=max(k[i+1][j],k[i][j-1])
	print(k[0][-1])




for i in range(0,int(input())):
	ab()
