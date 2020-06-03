def mat_mul(a,b):
	n = len(a) #we know a and b are of same size n x n
	#multiplication starts
	ans = [[0 for i in range(0,n)] for i in range(0,n)]
	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
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

n = int(input("Enter size: ")) #only square matrices can be raised to a power
mat = []
print("Enter matrix:")
for i in range(0, n):
    mat.append(list(map(int, input().split(' '))))
exp = int(input("Enter power: "))

ans = mat_power(mat,exp)

print("Product matrix:")
for i in range(0,n):
    for j in range(0,n):
        print(ans[i][j], end=" ")
    print()

'''OUTPUT:
Enter size: 3
Enter matrix:
1 0 0
0 1 0
0 0 1
Enter power: 7
Product matrix:
1 0 0 
0 1 0 
0 0 1

Enter size: 3
Enter matrix:
1 2 1
0 1 1
0 0 2
Enter power: 4
Product matrix:
1 8 37 
0 1 15 
0 0 16

Enter size: 2
Enter matrix:
1 2
2 1
Enter power: 10
Product matrix:
29525 29524 
29524 29525
'''
