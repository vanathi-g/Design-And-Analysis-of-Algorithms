def partition(arr, low, high):
	#sort bolts using nuts
	i = low
	j = low
	pivot = arr[high]
	while(j < high):
		if arr[j] < pivot:
			arr[i], arr[j] = arr[j], arr[i]
			i+=1
		j+=1
	arr[i], arr[high] = arr[high], arr[i]
	return i

def quicksort(a, low, high):
	if low>=high:
		return
	pivot = partition(a, low, high)
	quicksort(a, low, pivot-1)
	quicksort(a, pivot+1, high)

	
	
nuts = list(map(int, input("Enter nuts: ").split(' ')))
bolts = list(map(int, input("Enter bolts: ").split(' ')))
quicksort(nuts, 0, len(nuts)-1)
quicksort(bolts, 0, len(bolts)-1)
for i in range(0,len(nuts)):
	print(nuts[i]," matched with",bolts[i])
	
''' OUTPUT:
Enter nuts: 2 1 7 4 5 6
Enter bolts: 6 5 1 4 7 2
1  matched with 1
2  matched with 2
4  matched with 4
5  matched with 5
6  matched with 6
7  matched with 7
'''
