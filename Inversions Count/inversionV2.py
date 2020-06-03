def invCount(arr):
	n = len(arr)
	if n == 1:
		return arr,0
	mid = n//2
	l_arr, lc = invCount(arr[:mid])
	r_arr, rc = invCount(arr[mid:])
	i = 0
	j = 0
	temp=[]
	count=lc+rc
	while(i < mid and j < n-mid):
		if(l_arr[i] > r_arr[j]):
			count+=mid-i
			temp.append(r_arr[j])
			j+=1
		else:
			temp.append(l_arr[i])
			i+=1
	while(i<mid):
		temp.append(l_arr[i])
		i+=1
	while(j<n-mid):
		temp.append(r_arr[j])
		j+=1
	return temp, count

arr = list(map(int, input("Enter array: ").split(' ')))
ans, count = invCount(arr) 
print("Number of inversions =",count)

'''OUTPUT:
Enter array: 2 4 1 3 5
Number of inversions = 3

Enter array: 4 5 2 1 3
Number of inversions = 7

Enter array: 5 4 3 2 1
Number of inversions = 10

Enter array: 1 2 3 4 5
Number of inversions = 0

Enter array: 4 5 2 1 3
Number of inversions = 7
'''

#TIME COMPLEXITY: O(n*log(n)) ==>Linearithmic
