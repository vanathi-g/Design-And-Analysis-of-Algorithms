def max_subarray_sum_linear(arr):
	l = len(arr)
	maxSubSums = [0 for i in range(0,l)]
	maxSubSums[0] = arr[0]
	ind = [0 for i in range(0,l)]
	#first find max possible sum for all indices
	for i in range(1,l):
		maxSubSums[i]=max(maxSubSums[i-1]+arr[i],arr[i])
		if(maxSubSums[i] == arr[i]):
			ind[i]=1
	#now find the maximum subarray sum
	maxSum = -10000
	start=0
	end=0
	for i in range(0,l):
		if(maxSubSums[i]>maxSum):
			maxSum = maxSubSums[i]
			end=i
	for i in range(end-1,-1,-1):
		if(ind[i]==1):
			start=i
			break
	return start, end, maxSum

arr = list(map(int, input("Enter array: ").split(' ')))
ans = max_subarray_sum_linear(arr)
print("Max subarray is",arr[ans[0]:ans[1]+1])
print("Max sum =",ans[2])

'''OUTPUT:
Enter array: -2 -4 3 -1 5 6 -7 -2
Max subarray is [3, -1, 5, 6]
Max sum = 13
'''