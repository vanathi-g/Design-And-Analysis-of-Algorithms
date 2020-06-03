def findMaxLenSub(arr):
	l = len(arr)
	dp = [1 for i in range(0,l)]
	pred = [i for i in range(0,l)]
	for i in range(0,l):
		for j in range(0,i+1):
			if arr[j] < arr[i]:
				if dp[j]+1 > dp[i]:
					dp[i] = dp[j]+1
					pred[i] = j
	return dp, pred

arr = list(map(int, input("Enter array: ").split(' ')))
lens, pred = findMaxLenSub(arr)
i = pred[-1]
ele=[]
ele.append(arr[-1])
while(True):
	ele.append(arr[i])
	if pred[i]==i:
		break
	i = pred[i]

print("Longest Increasing Subsequence is:",' '.join(map(str,ele[::-1])))

''' OUTPUT - 
Enter array: 5 2 8 6 3 6 9 7
Longest Increasing Subsequence is: 2 3 6 7

Enter array: 5 1 5 7 2 4 9 8
Longest Increasing Subsequence is: 1 5 7 8

Enter array: 3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6
Longest Increasing Subsequence is: 1 2 3 5 6
'''
