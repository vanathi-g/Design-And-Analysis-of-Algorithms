from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def findMaxLenSub(arr,j):
    temp=arr[:j]
    p=powerset(temp)
    max=0
    mst=[]
    for i in range(2**j):
        subs=list(p[i])
        if(sorted(subs)):
            if(len(subs)>max):
                max=len(subs)
                mst=subs
    return mst,max

arr = list(map(int, input("Enter array: ").split(' ')))
subS, maxLen = findMaxLenSub(arr,len(arr))
print("Longest Increasing Subsequence is:",subS)

'''OUTPUT:
Enter array: 5 2 8 6 3 6 9 7
Longest Increasing Subsequence is: [5, 6, 6, 9]
'''
