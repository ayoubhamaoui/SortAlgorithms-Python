# Sort Algorithms in Python
>>In computer science, a sorting algorithm is an algorithm that puts elements of a list in a certain order. The most-used orders are numerical order and lexicographical order. Efficient sorting is important for optimizing the use of other algorithms (such as search and merge algorithms) which require input data to be in sorted lists; it is also often useful for canonicalizing data and for producing human-readable output. More formally, the output must satisfy two conditions:
>>1. The output is in nondecreasing order (each element is no smaller than the previous element according to the desired total order);
>>2. The output is a permutation (reordering) of the input.

## I.Merge Sort:
The key operation of the merge sort algorithm is the merging of two sorted
sequences in the “combine” step. We merge by calling an auxiliary procedure
MERGE(A,p,q,r), where A is an array and p, q, and r are indices into the array
such that p <= q < r. The procedure assumes that the subarrays A[p..q] and
A[q+1..r] are in sorted order. It merges them to form a single sorted subarray
that replaces the current subarray A[p..r].

The procedure MERGE-SORT(A,p,r) sorts the elements in the subarray
A[p..r]. If p>=r, the subarray has at most one element and is therefore
already sorted. Otherwise, the divide step simply computes an index q that partitions
A[p..r] into two subarrays: A[p..q], containing E[n/2]-1 elements, and
A[q+1..r], containing E[n/2]+1 elements.
![image](http://mikebuss.com/images/posts/merge-sort/MergeSort.png)

### Code Python:
```python
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
                Merge(A,p,q,r)s
```


* References:
>> 1. Wikipedia
>> 2. Introduction to algorithms
