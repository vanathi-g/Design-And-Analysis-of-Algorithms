def max_subarray_sum_cubic(arr):
	n = len(arr)
	max_l = 0
	max_r = 0
	maxSum = -10000
	for i in range(0,n):
		for j in range(i+1,n):
			sums = 0
			for k in range(i,j):
				sums+=arr[k]
			if(maxSum < sums):
				maxSum = sums
				max_l = i
				max_r = j
	return max_l, max_r, maxSum
			
arr = list(map(int, input("Enter array: ").split(' ')))
ans = max_subarray_sum_cubic(arr)
print("Max subarray is from:",ans[0],"to",ans[1])
print("Max sum =",ans[2])

'''OUTPUT:
Enter array: -2 -4 3 -1 5 6 -7
Max subarray is from: 2 to 6
Max sum = 13
'''

