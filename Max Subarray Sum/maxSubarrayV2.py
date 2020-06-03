def prefixSum(arr):
	psum = [0 for i in range(0,len(arr))]
	psum[0] = arr[0]
	for i in range(1, len(arr)):
		psum[i] = psum[i-1]+arr[i]
	return psum
	
def max_subarray_sum_quadratic(arr):
	n = len(arr)
	max_l = 0
	max_r = 0
	maxSum = -10000
	subSum = 0
	psum = prefixSum(arr)
	for i in range(0,n):
		for j in range(i,n):
			if(i==j):
				subSum = psum[j]
			else:
				subSum = psum[j]-psum[i]
			if(subSum > maxSum):
				maxSum = subSum
				max_l = i+1
				max_r = j
	return max_l, max_r, maxSum
	
arr = list(map(int, input("Enter array: ").split(' ')))
ans = max_subarray_sum_quadratic(arr)
print("Max subarray is",arr[ans[0]:ans[1]+1])
print("Max sum =",ans[2])

'''OUTPUT:
Enter array: -2 -4 3 -1 5 6 -7 -2
Max subarray is [3, -1, 5, 6]
Max sum = 13
'''