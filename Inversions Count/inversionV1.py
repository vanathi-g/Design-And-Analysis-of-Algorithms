def invCount(arr):
	count=0
	n=len(arr)
	for i in range(0,n):
		for j in range(i,n):
			if(arr[i] > arr[j]):
				count+=1
	return count

arr = list(map(int, input("Enter array: ").split(' ')))
ans = invCount(arr) 
print("Number of inversions =",ans)

'''OUTPUT:
Enter array: 2 4 1 3 5
Number of inversions = 3

Enter array: 4 5 2 1 3
Number of inversions = 7

Enter array: 5 4 3 2 1
Number of inversions = 10
'''

#TIME COMPLEXITY: O(n^2) ==>Quadratic
