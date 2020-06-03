def ordered_insert(u,v):
    n = len(v)
    if n == 0 or v[n-1] < u:
        v.append(u)
        return v
    return (ordered_insert(u,v[:n-1])+v[n-1:])

arr = list(map(int, input("Enter sorted list of numbers: ").split(' ')))
num = int(input("Enter number to insert: "))
arr = ordered_insert(num, arr)
print("List after inserting: ", arr)

'''OUTPUT:
Enter sorted list of numbers: 4 12 17 19 11
Enter number to insert: 15
List after inserting:  [4, 12, 17, 19, 11, 15]
'''
