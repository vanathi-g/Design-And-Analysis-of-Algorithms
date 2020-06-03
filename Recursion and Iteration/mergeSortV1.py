def ordered_insert(u,v):
    n = len(v)
    if n == 0 or v[n-1] < u:
        v.append(u)
        return v
    return (ordered_insert(u,v[:n-1])+v[n-1:])

def ordered_merge(u, v):
    for num in u:
        v = ordered_insert(num,v)
    return v

arr1 = list(map(int, input("Enter sorted list 1: ").split(' ')))
arr2 = list(map(int, input("Enter sorted list 2: ").split(' ')))
ans = ordered_merge(arr1, arr2)
print("Merged lists:", ans)

'''OUTPUT:
Enter sorted list 1: 2 5 7 9 11
Enter sorted list 2: 1 3 4 8 10
Merged lists: [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
'''
