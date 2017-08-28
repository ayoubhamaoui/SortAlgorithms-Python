def Merge(A,p,q,r):
	n1=q-p+1
	n2=r-q
	L=[]
	R=[]
	for i in range(n1):
		L.append(A[p+i-1])
	for j in range(n2):
		R.append(A[q+j])
	i=j=0
	L.append(float( "inf" ))
	R.append(float("inf"))
	print("L=",L)
	print("R=",R)
	for k in range(len(A)):
		if(L[i]<=R[j]):
			A[k]=L[i]
			i=i+1
		else:
			A[k]=R[j]
			j=j+1
		print("A1=",A)
	print("A2=",A)





def MergeSort(A,p,r):
        if(p<r):
                q=(p+r)/2
                MergeSort(A,p,q)
                MergeSort(A,q+1,r)
                Merge(A,p,q,r)
        

                
