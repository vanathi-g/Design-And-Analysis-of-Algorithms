def max_subarray_sum_linearithmic(arr):

    l = len(arr)

    if l == 1: 
        return arr[0]

    mid = l//2
    l_sum = max_subarray_sum_linearithmic(arr[:mid])
    r_sum =  max_subarray_sum_linearithmic(arr[mid:])
    
    #finding max subarray overlapping both halves
    #step 1: find max suffix of first half
    sums = 0
    maxLeft = -10000
    for i in range(mid, -1, -1):
        sums+=arr[i]
        if(sums > maxLeft):
            maxLeft = sums

    #step 2: find max prefix of second half
    sums = 0
    if l!= 2:
        maxRight = -10000
    else:
        maxRight = 0
    for i in range(mid+1, l):
        sums+=arr[i]
        if(sums > maxRight):
            maxRight = sums

    #step 3: return maximum of the three values
    return max(l_sum, r_sum, (maxRight+maxLeft));


arr = list(map(int, input("Enter array: ").split(' ')))
ans = max_subarray_sum_linearithmic(arr)

print("Max sum =",ans)

'''OUTPUT:
Enter array: -2 -4 3 -1 5 6 -7 -2
Max sum = 13
'''