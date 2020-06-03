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

m1, n1 = map(int, input("Enter size of Mat1: ").split(' '))
m2, n2 = map(int, input("Enter size of Mat2: ").split(' '))
if n1 == m2:
        mat1 = []
        mat2 = []
        print("Enter matrix 1:")
        for i in range(0, m1):
                mat1.append(list(map(int, input().split(' '))))
        print("Enter matrix 2:")
        for i in range(0,m2):
                mat2.append(list(map(int, input().split(' '))))
        ans = mat_mul(mat1, mat2)
        print("Product matrix:")
        for i in range(0,m1): #size of prod m1 x n2
                for j in range(0,n2):
                        print(ans[i][j], end=" ")
                print()
else:
        print("Incompatible matrices")
			
'''OUTPUT:
Enter size of Mat1: 2 3
Enter size of Mat2: 3 1
Enter matrix 1:
2 4 6
1 2 3
Enter matrix 2:
1
0
1
Product matrix:
8 
4 

Enter size of Mat1: 3 3
Enter size of Mat2: 3 3
Enter matrix 1:
1 2 3
4 5 6
7 8 9
Enter matrix 2:
1 0 0
0 1 0
0 0 1
Product matrix:
1 2 3 
4 5 6 
7 8 9 

Enter size of Mat1: 1 2
Enter size of Mat2: 3 1
Incompatible matrices
'''
