def ordered_insert(u,v):
    n = len(v)
    if n == 0 or v[n-1] < u:
        v.append(u)
        return v
    return (ordered_insert(u,v[:n-1])+v[n-1:])

def merge(u, v):
    for num in u:
        v = ordered_insert(num,v)
    return v

def MergeSort(a):
    l = len(a)
    if l<=1:
        return a
    return merge(MergeSort(a[:l//2]),MergeSort(a[l//2:]))
    
arr = list(map(int, input("Enter list of numbers: ").split(' ')))
arr = MergeSort(arr)
print("Sorted list:",arr)

'''OUTPUT:
Enter list of numbers: 4 1 99 12 18 32 3
Sorted list: [1, 3, 4, 12, 18, 32, 99]
'''
