def mat_mul(a,b):
	m1 = len(a)
	n1 = len(a[0])
	n2 = len(b[0])
	#multiplication starts
	ans = [[0 for i in range(0,n2)] for i in range(0,m1)]
	for i in range(0,m1):
		for j in range(0,n1):
			for k in range(0,n2):
				ans[i][k] += a[i][j]*b[j][k]
	return ans

def identity(n): #generates identity matrix of order n x n
    ans = [[0 for i in range(0,n)] for i in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                ans[i][j]=1
    return ans

def mat_power(x,n):
	if n==0:
		return identity(len(x)) #identity matrix is the multiplicative identity
	if n%2==0:
		ans = mat_power(x,n-1)
	else:
		ans = mat_mul(mat_power(x,n//2),mat_power(x,n//2))
	return mat_mul(x,ans)
    
def fib(n):
    fibMat = [[0,1],[1,1]]
    return (mat_mul(mat_power(fibMat,n), [[0],[1]]))

n = int(input("Enter number of terms: "))
for i in range(1,n+1,2):
    terms = fib(i)
    print(terms[0][0], end=' ')
    if i==n and n%2!=0:
        break
    print(terms[1][0], end=' ')

'''OUTPUT:
Enter number of terms: 3
1 1 2
Enter number of terms: 6
1 1 2 3 5 8
'''
